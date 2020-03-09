import json
from Lambda_Layer import Lambda_Layer
from Globals import Globals

def lambda_handler(event, context):
    if event['body'] is None:
        return bad_request("body")
    postdata                    = json.loads(event['body'])
    if("name" not in postdata):
        return bad_request("name")
    name                        = postdata['name'].replace('.', '-')
    folders_mapping             = None
    description = None
    if 'description' in postdata:
        description             = postdata['description']
    s3_bucket = Globals.lambda_layers_s3_bucket
    if 's3_bucket' in postdata:
        s3_bucket               = postdata['s3_bucket']
    lambda_layer                = Lambda_Layer(name, folders_mapping, s3_bucket, description)
    lambda_layer.create()
    return ok()


def ok():
    return {
        'statusCode': 200,
        'body': json.dumps('Layer Created!')
    }


def bad_request(parameter_name):
    return {
        'statusCode': 400,
        'body': f'Missing parameter - {parameter_name}'
    }