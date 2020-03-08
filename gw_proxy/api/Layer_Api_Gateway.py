from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.Session import Session
from osbot_utils.decorators.Method_Wrappers import cache, catch, remove
from osbot_aws.tmp_utils.Temp_Misc import Temp_Misc
from osbot_aws.apis.S3 import S3
from gw_proxy._to_sync.anish_agarwal.Proxy_Const import *
import time
from osbot_aws.apis.IAM import IAM

class Layer_Api_Gateway:
    def __init__(self, name=None, folders_mapping={}, s3_bucket=None, description=''):
        self.runtime            = None
        self.memory             = 0
        self.timeout            = 0
        self.trace_mode         = None
        self.handler            = None
        self.name               = None
        self.folder_code        = None
        self.role               = None
        self.s3_bucket          = None
        self.s3_key             = None
        self.api_gateway        = Session().client('apigateway')
        self.api_name           = None

    @cache
    def client(self):
        return Session().client('lambda')

    # The actual api to invoke to add the api route to layers creation/deletion
    def create_infrastructure(self):
        '''create lambda to create layers'''
        self.runtime            = LAMBDA_RUNTIME
        self.memory             = LAMBDA_MEMORY
        self.timeout            = LAMBDA_TIMEOUT
        self.trace_mode         = LAMBDA_TRACE_MODE
        self.handler            = "lambda.handler"
        self.name               = AWS_CREATE_LAYER_LAMBDA_NAME
        self.folder_code        = AWS_LAYER_ADD_CODE_DIR_PATH + "creator.zip"
        self.role               = AWS_LAMBDA_ROLE_ARN
        self.s3_bucket          = AWS_S3_BUCKET
        ts                      = time.time()
        self.s3_key             = "creator_" + str(ts)
        self.create_lambda()
        '''create apig route to above lambda'''
        self.create_rest_api(self,API_GW_PATH_CREATE_LAYER,"POST",AWS_CREATE_LAYER_LAMBDA_NAME)
        '''create lambda to delete layers'''
        self.name = AWS_DELETE_LAYER_LAMBDA_NAME
        self.folder_code = AWS_LAYER_ADD_CODE_DIR_PATH + "remover.zip"
        ts = time.time()
        self.s3_key = "deleter_" + str(ts)
        self.create_lambda()
        '''create apig route to above lambda'''
        self.create_rest_api(self, API_GW_PATH_DELETE_LAYER, "POST", AWS_DELETE_LAYER_LAMBDA_NAME)

    #######################################        LAMBDA HANDLERS        ##############################################

    def create_lambda(self):
        missing_fields = Temp_Misc.get_missing_fields(self,['name', 'runtime', \
                         'role','handler', 'memory','timeout','s3_bucket', 's3_key'])
        if len(missing_fields) > 0:
            return { 'error': 'missing fields in create_function: {0}'.format(missing_fields) }

        (name, runtime, role, handler, memory_size, timeout, tracing_config, code) = self.create_params()

        if self.exists() is True:
            return {'status': 'warning', 'name': self.name, 'data': 'lambda function already exists'}

        if self.s3().file_exists(code.get('S3Bucket'), code.get('S3Key')) is False:
            return {'status': 'error', 'name': self.name, 'data': 'could not find provided s3 bucket and s3 key'}

        try:
            data = self.client().create_function(
                FunctionName            = name,
                Runtime                 = runtime,
                Role                    = role,
                Handler                 = handler,
                MemorySize              = memory_size,
                Timeout                 = timeout,
                TracingConfig           = tracing_config,
                Code                    = code
            )

            return { 'status': 'ok', 'name': self.name , 'data' : data }
        except Exception as error:
            return {'status': 'error', 'data': '{0}'.format(error)}


    def create_params(self,params):
        FunctionName            = params.name
        Runtime                 = params.runtime
        Role                    = params.role
        Handler                 = params.handler
        MemorySize              = params.memory
        Timeout                 = params.timeout
        TracingConfig           = { 'Mode': self.trace_mode }
        Code                    = { "S3Bucket" : self.s3_bucket, "S3Key": params.s3_key}
        return                    FunctionName, Runtime, Role, Handler, MemorySize, Timeout, TracingConfig, Code


    @cache
    def s3(self):
        return S3()

    def upload(self):
        self.s3().folder_upload(self.folder_code, self.s3_bucket, self.s3_key)
        return self.s3().file_exists(self.s3_bucket, self.s3_key)

    @remove('ResponseMetadata')
    def info(self):
        return self.client().get_function(FunctionName=self.name)

    def exists(self):
        try:
            self.info()
            return True
        except:
            return False

    def set_role                    (self, value): self.role            = value    ; return self
    def set_s3_bucket               (self, value): self.s3_bucket       = value    ; return self
    def set_s3_key                  (self, value): self.s3_key          = value    ; return self
    def set_folder_code             (self, value): self.folder_code     = value    ; return self
    def set_trace_mode              (self, value): self.trace_mode      = value    ; return self
    def set_timeout                 (self, value): self.timeout         = value    ; return self
    def set_runtime                 (self, value): self.runtime         = value    ; return self
    def set_memory                  (self, value): self.memory          = value    ; return self
    def set_folder_code             (self, value): self.folder_code     = value    ; return self
    def set_name                    (self, value): self.name            = value    ; return self


    ##########################################        API GATEWAY        ###############################################

    def create_rest_api(self,path,method,lambda_name):
        self.path                       = path
        self.method                     = method
        self.lambda_name                = lambda_name
        self.parent_api_id              = self.rest_api_create(self.api_name)
        self.resources                  = self.resources(self.parent_id)
        self.base_resouce_id            = self.resources[0].id
        self.resource_id                = self.resource_create(self, self.parent_api_id, self.base_resouce_id, path)
        self.method_id                  = self.method_create(self, self.parent_api_id, self.resource_id, "POST")
        self.lambda_integration_result  = self.add_method_lambda(self, path, "POST", lambda_name)
        return self

    def resource_create(self, api_id, parent_id, path):
        return self.api_gateway.create_resource(restApiId=api_id, parentId=parent_id,pathPart=path)

    def method_create(self, api_id, resource_id, http_method, authorization_type='NONE'):
        return self._call_method(
            "put_method", {
                'restApiId'                 : api_id,
                'resourceId'                :resource_id,
                'httpMethod'                :http_method,
                'authorizationType'         :authorization_type
            }
        )

    def add_method_lambda(self, from_path, from_method, lambda_name):
        resource_id                         = self.resource_id(from_path)
        status_code                         = '200'
        response_models                     = {'application/json': 'Empty'}
        response_templates                  = {'application/json': ''}
        method_create                       = self.api_gateway.method_create(self.api_id, resource_id,from_method)
        integration_create__lambda          = self.api_gateway.integration_create__lambda(self.id(), resource_id, lambda_name,from_method)
        integration_add_permission          = self.api_gateway.integration_add_permission_to_lambda(self.id(), lambda_name)
        method_response_create              = self.api_gateway.method_response_create(self.id(),resource_id,from_method, status_code,response_models)
        integration_response_create         = self.api_gateway.integration_response_create(self.id(),resource_id, from_method,status_code, response_templates)
        return {
             'method_create'                 : method_create               ,
             'integration_create__lambda'   : integration_create__lambda    ,
             'integration_add_permission'   : integration_add_permission,
             'method_response_create'       : method_response_create      ,
             'integration_response_create'  : integration_response_create
        }

    def integration_add_permission_to_lambda(self,api_id, lambda_name):
        iam                                 = IAM()
        aws_acct_id                         = iam.account_id()
        aws_region                          = iam.region()
        aws_lambda                          = Lambda(lambda_name)
        function_arn                        = aws_lambda.function_Arn()
        statement_id                        = 'allow-api-gateway-invoke'
        action                              = 'lambda:InvokeFunction'
        principal                           = 'apigateway.amazonaws.com'
        source_arn                          = f'arn:aws:execute-api:{aws_region}:{aws_acct_id}:{api_id}/*/*/'

        aws_lambda.permission_delete(function_arn, statement_id) # remove in case there was already a permission with this name
        return aws_lambda.permission_add(function_arn, statement_id, action, principal, source_arn)

    def integration_create__lambda(self, api_id, resource_id, lambda_name, http_method):
        iam         = IAM()
        aws_acct_id = iam.account_id()
        aws_region  = iam.region()

        input_type = 'AWS_PROXY'
        uri = f'arn:aws:apigateway:{aws_region}:lambda:path/2015-03-31/functions/arn:aws:lambda:{aws_region}:{aws_acct_id}:function:{lambda_name}/invocations'
        integration_http_method = 'POST'
        try:
            return self.api_gateway.put_integration(
                restApiId               = api_id,
                resourceId              = resource_id,
                httpMethod              = http_method,
                integrationHttpMethod   = integration_http_method,type=input_type, uri=uri)
        except Exception as error:
            return f'{error}'

    def method_response_create(self,api_id,resource_id,http_method,status_code,response_models):
        params = { 'restApiId'     : api_id ,
                   'resourceId'    : resource_id ,
                   'httpMethod'    : http_method ,
                   'statusCode'    : status_code ,
                   'responseModels': response_models
                   }
        return self._call_method('put_method_response', params)

    def integration_response_create(self, api_id, resource_id, http_method, status_code,response_templates):
        params = {'restApiId'        : api_id,
                  'resourceId'       : resource_id,
                  'httpMethod'       : http_method,
                  'statusCode'       : status_code,
                  'responseTemplates': response_templates
                  }
        return self._call_method('put_integration_response', params)

    def rest_api_create(self, api_name):
        rest_apis = self.rest_apis(index_by='name')
        if api_name in rest_apis:
            return rest_apis.get(api_name)
        params = {
            'name'                       : api_name,
            'endpointConfiguration'      : {"types": ["REGIONAL"]}}

        return self.api_gateway.create_rest_api(**params)

    def resources(self, api_id_or_name, index_by='id'):
        result = self._get_using_api_id('resources', api_id=api_id_or_name, index_by=index_by)
        if result.get('error') is None:
            return result
        rest_apis = self.rest_apis(index_by='name')
        if api_id_or_name in rest_apis:
            api_id = rest_apis.get(api_id_or_name).get('id')
            return self._get_using_api_id('resources', api_id=api_id, index_by=index_by)
        return {'error': f'API not found: {api_id_or_name}'}


    def _get_using_api_id(self, target, api_id, index_by='id', data_key='items'):
        return self._call_method_return_items(method_name=f"get_{target}", params={'restApiId': api_id}, index_by=index_by, data_key=data_key)

    def rest_apis(self, index_by='id'):
        return self._call_method_return_items(method_name="get_rest_apis",index_by=index_by)

    def _call_method(self, method_name, params):
        try:
            return getattr(self.api_gateway, method_name)(**params)
        except Exception as error:
            return {'error': f'{error}'}

    def _call_method_return_items(self, method_name, params={}, index_by='id', data_key='items'):
        try:
            raw_data = getattr(self.api_gateway, method_name)(**params)
            data = {}
            for item in raw_data.get(data_key):
                data[item.get(index_by)] = item
            return data
        except Exception as error:
            return {'error' : f'{error}'}
