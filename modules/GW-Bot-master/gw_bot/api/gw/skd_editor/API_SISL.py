import json

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files


class API_SISL:
    def __init__(self):
        self.tag_names   = ['FileStream','DOCUMENT','STRUCTARRAY', 'VALUEARRAY',
                            'STRUCT','VALUE',
                            'ITEM']
        self.field_names = ['cameraname','streamname', '__children',
                            'name', 'estrc','offset','size', 'eitem',
                            '__data']

    def convert_sisl_file_to_json(self, path_to_file):
        sisl_data = Files.contents(path_to_file)
        return self.convert_sisl_to_json(sisl_data)

    def convert_sisl_to_json(self, sisl_data):
        mappings = [  ('__struct'      , '"__struct'     ),
                      ('__meta: !__'   , '"meta":'       )]

        for tag_name in self.tag_names:
            mappings.append((f'!{tag_name}', f'{tag_name}":'))

        for field_name in self.field_names:
            mappings.append((f'{field_name}: !__', f'"{field_name}":'))

        json_data = sisl_data
        for key, value in mappings:
            json_data = json_data.replace(key,value)
        return json.loads(json_data)

    def convert_json_to_sisl(self, json_data):

        mappings = [('"__struct', '__struct'    ),
            ('"meta":'  , '__meta: !__' )]

        for tag_name in self.tag_names:
            mappings.append((f'{tag_name}":', f'!{tag_name}'))

        for field_name in self.field_names:
            mappings.append((f'"{field_name}":', f'{field_name}: !__'))

        sisl_data = json.dumps(json_data,indent=2)
        for key, value in mappings:
            sisl_data = sisl_data.replace(key, value)
        return sisl_data

    def convert_json_to_sisl_file(self, json_data, sisl_file):
        sisl_data = self.convert_json_to_sisl(json_data)
        Files.write(sisl_file, sisl_data)
        return sisl_file

    def edit_value_array(self, target_folder, stream_id, struct_id, new_value):

        matches = Files.find(f'{target_folder}/*stream_{stream_id}*.sisl')
        if len(matches) == 1:
            sisl_file = matches.pop()
            json_data = self.convert_sisl_file_to_json(sisl_file)
            key = f"__struct_{struct_id}: VALUEARRAY"
            if json_data[key]:
                json_data[key]['__data'] = new_value
                return self.convert_json_to_sisl_file(json_data,sisl_file)
        return False
            #self.sisl.edit_value_array(target_folder, "5", "620", "NEW VALUE!!!!")

    def unzip_sisl_file(self, sisl_zip_file):
        file_name = Files.file_name(sisl_zip_file).replace('.zip','')
        temp_folder = Files.temp_folder(suffix='-' + file_name, parent_folder='/tmp')
        return Files.unzip_file(sisl_zip_file, temp_folder)

    def zip_sisl_files(self, folder_with_sisl_files):
        return Files.zip_folder(folder_with_sisl_files)


    def mappings(self, sisl_file, max_entries=None):
        json_data = self.convert_sisl_file_to_json(sisl_file)

        def get_children(node):
            children = node.get('__children')
            if children is None:
                return []
            left, right = node.get('__children').split("-")
            if left == right:
                return [left]
            else:
                return [left, right]

        mappings = {}

        for node_key, node_data in json_data.items():
            (node_id, node_type) = node_key.replace('__struct_', '').split(': ')
            mappings[node_id] = {
                'type': node_type,
                'children': get_children(node_data),
                'raw': node_data
            }
            if max_entries and len(mappings) > max_entries:
               break

        return mappings

    def process_item_recursively(self, key, current_depth, results, json_data):
        #print(f'>>> at {key} key with {current_depth} depth')
        item = json_data[key]
        results[key] = item
        if current_depth > 0:
            #print(f'Recursive: {key} {current_depth}')
            current_depth -= 1
            for child_key in item['children']:
                #print(item['children'])
                self.process_item_recursively(child_key, current_depth, results, json_data)

        #print(f'return from {key} with depth {current_depth}')

    def create_mappings_view(self,sisl_file, start_id, max_depth):

        print('-------')
        results = {}
        json_data   = self.mappings(sisl_file)
        root_key    = str(start_id)
        #root_item   = json_data[root_key]
        self.process_item_recursively(root_key, max_depth, results, json_data)

        return results