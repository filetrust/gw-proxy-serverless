from osbot_aws.apis.Lambda import Lambda
from osbot_aws.apis.API_Gateway import API_Gateway
from osbot_aws.apis.Session import Session
from osbot_aws.helpers.Rest_API import Rest_API
from osbot_utils.decorators.Method_Wrappers import cache, catch, remove
from osbot_aws.tmp_utils.Temp_Misc import Temp_Misc
from osbot_aws.apis.S3 import S3
from gw_proxy._to_sync.anish_agarwal.Proxy_Const import *
import time
from osbot_aws.apis.IAM import IAM


class Layer_Api_Gateway:

    def __init__(self):
        self.runtime = None
        self.memory = 0
        self.timeout = 0
        self.trace_mode = None
        self.handler = None
        self.name = None
        self.folder_code = None
        self.role = None
        self.s3_bucket = None
        self.s3_key = None
        self.api_gateway = Session().client('apigateway')
        self.api_name = None

    @cache
    def client(self):
        return Session().client('lambda')

    # The actual api to invoke to add the api route to layers creation/deletion
    def create_infrastructure(self):
        '''create lambda to create layers'''
        self.runtime = LAMBDA_RUNTIME
        self.memory = LAMBDA_MEMORY
        self.timeout = LAMBDA_TIMEOUT
        self.trace_mode = LAMBDA_TRACE_MODE
        self.handler = "lambda.handler"
        self.name = AWS_CREATE_LAYER_LAMBDA_NAME
        self.folder_code = AWS_LAYER_ADD_CODE_DIR_PATH + "creator.zip"
        self.role = AWS_LAMBDA_ROLE_ARN
        self.s3_bucket = AWS_S3_BUCKET
        ts = time.time()
        self.s3_key = "creator_" + str(ts)
        self.create_lambda()
        '''create apig route to above lambda'''
        self.create_api_route(API_GW_PATH_CREATE_LAYER, "POST", AWS_CREATE_LAYER_LAMBDA_NAME)
        '''create lambda to delete layers'''
        self.name = AWS_DELETE_LAYER_LAMBDA_NAME
        self.folder_code = AWS_LAYER_ADD_CODE_DIR_PATH + "remover.zip"
        ts = time.time()
        self.s3_key = "deleter_" + str(ts)
        self.create_lambda()
        '''create apig route to above lambda'''
        self.create_api_route(self, API_GW_PATH_DELETE_LAYER, "POST", AWS_DELETE_LAYER_LAMBDA_NAME)

    #######################################        LAMBDA HANDLERS        ##############################################

    def create_lambda(self):
        try:
            data = self.client().create_function(
                FunctionName            = self.name,
                Runtime                 = self.runtime,
                Role                    = self.role,
                Handler                 = self.handler,
                MemorySize              = self.memory_size,
                Timeout                 = self.timeout,
                TracingConfig           = self.tracing_config,
                Code                    = self.code
            )
            return {'status': 'ok', 'name': self.name, 'data': data}
        except Exception as error:
            return {'status': 'error', 'data': '{0}'.format(error)}

    ##########################################        API GATEWAY        ###############################################

    def create_api_route(self, path, method, lambda_name):
        self.path                       = path
        self.method                     = method
        self.lambda_name                = lambda_name
        rest_api                        = Rest_API(self.api_name)
        api_creation_response           = rest_api.create()
        parent_api_id                   = api_creation_response["id"]
        api_gateway                     = API_Gateway()
        path_id                         = api_gateway.resource(parent_api_id, '/').get('id')
        # create resource
        resource_id                     = api_gateway.resource_create(parent_api_id, path_id, path).get('id')
        api_gateway.method_create(parent_api_id, resource_id, method)
        api_gateway.integration_create__lambda(api_id=parent_api_id,
                    resource_id=resource_id,lambda_name=lambda_name, http_method=method)
        self.integration_add_permission_to_lambda(lambda_name)
        return self


if __name__ == '__main__':
    apig = Layer_Api_Gateway()
    apig.create_infrastructure()