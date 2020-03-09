CONST_STACKOVERFLOW            = 'stackoverflow'
CONST_GLASSWALL                = 'glasswall'
CONST_GW_PROXY                 = 'gw-proxy'

CONST_DEFAULT_SITE             = 'glasswall-file-drop.azurewebsites.net'
CONST_SITE_STACKOVERFLOW       = 'stackoverflow.com'
CONST_SITE_GLASSWALL           = 'www.glasswallsolutions.com'

CONST_BINARY_TYPES             = [  "application/octet-stream"  ,
                                    "application/x-protobuf"    ,
                                    "application/x-tar"         ,
                                    "application/zip"           ,
                                    "image/png"                 ,
                                    "image/jpeg"                ,
                                    "image/jpg"                 ,
                                    "image/tiff"                ,
                                    "image/webp"                ,
                                    "image/jp2"                 ,
                                    'font/woff'                 ,
                                    'font/woff2'                ,
                                    'text/html; charset=UTF-8'  ]

CONST_ORIGINAL_GW_SITE         = 'glasswallsolutions.com'
CONST_REPLACED_GW_SITE         = 'glasswall.gw-proxy.com'

CONST_ORIGINAL_STACKOVERFLOW   = 'Stack Overflow'
CONST_REPLACED_STACKOVERFLOW   = '<b>[CHANGED BY THE PROXY]</b>'

CONST_SCHOOL_STEM              = 'School STEM show hits the road'
CONST_REPLACED_SCHOOL_STEM     = 'BAE STOP with "Glasswall Inside" available in March 2020'

CONST_PARTNERED                = 'We have partnered with Royal Airforce and Royal Navy to take STEM to The Belvedore Academy in Liverpool'
CONST_REPLACED_PARTNERED       = 'Product available for pre-order at the <a href="http://glasswall-store.com/">Glasswall Store</a>'

CONST_BAE_SYSTEMS_IMG          = 'https://www.baesystems.com/en/download-en/multimediaimage/webImage/20200214163601/1434644561633.jpg'
CONST_REPLACED_BAE_SYSTEMS_IMG = 'https://user-images.githubusercontent.com/656739/74657297-d5f10a00-5187-11ea-908a-e9f8ca79d1fa.png'
CONST_ANGER                    = 'Anger as historic car brand scrapped in Australia'
CONST_REPLACED_ANGER           = 'BAE STOP with "Glasswall Inside" available in March 2020'

CONST_US_CAR_GIANT             = 'The move comes as the US car giant ' 'retreats from more markets to focus on more profitable countries.'
CONST_REPLACED_US_CAR_GIANT    = 'Product available for pre-order at the <a href="http://glasswall-store.com/">Glasswall Store</a>'

CONST_HEADER_BROTLI_ENCODING   = 'br'

RESPONSE_BAD_REQUEST           = 'Request body was invalid'
RESPONSE_SERVER_ERROR          = 'A server error was encountered while processing the request'

# Lambda and API Gateway Creation Constants
AWS_ACCOUNT_ID                 =  ''
AWS_ACCESS_ID                  =  ''
AWS_SECRET_KEY                 =  ''
AWS_REGION                     =  ''
AWS_LAMBDA_ROLE_ARN            =  ''

# To push lambda code temporarily before deployment
AWS_S3_BUCKET                  =  ''
AWS_CREATE_LAYER_LAMBDA_NAME   =  'Layers_Creator'
AWS_DELETE_LAYER_LAMBDA_NAME   =  'Layers_Remover'
AWS_LAYER_ADD_CODE_DIR_PATH    =  '../to_sync/anish_agarwal/lambda/creator/'
AWS_LAYER_DEL_CODE_DIR_PATH    =  '../to_sync/anish_agarwal/lambda/remover/'

# Lambda RUntime Configuration Constants
LAMBDA_RUNTIME                  =  'python3.8'
LAMBDA_MEMORY                   = 512
# Max timeout
LAMBDA_TIMEOUT                  = 900
LAMBDA_TRACE_MODE               = 'PassThrough'

# API Gw constants
API_GW_NAME                     = 'LayersApis'
API_GW_PATH_CREATE_LAYER        = '/create'
API_GW_PATH_DELETE_LAYER        = '/delete'