from configurations.cdk_config import LAMBDA_CONFIG
from constructs import Construct
import aws_cdk as core
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway,
    aws_iam as _iam
)

class UnstopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = _iam.Role(
            scope=self, id='unstop-cdk-lambda-role',
            assumed_by =_iam.ServicePrincipal('lambda.amazonaws.com'),
            role_name='unstop-cdk-lambda-role',
            managed_policies=[
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaVPCAccessExecutionRole'),
                _iam.ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole'),
                _iam.ManagedPolicy.from_aws_managed_policy_name('AdministratorAccess')
            ]
        )

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_apigateway/RestApi.html
        api = _apigateway.RestApi(
            self, 
            id='UnstopAPI',
            rest_api_name="UnstopAPI",
            default_cors_preflight_options = _apigateway.CorsOptions(
                allow_origins=["*"],
                allow_methods=["GET", "POST", "PUT", "DELETE"],
                allow_headers=["*"],
            ),
            endpoint_configuration = _apigateway.EndpointConfiguration(types=[_apigateway.EndpointType.REGIONAL]),
            deploy_options = _apigateway.StageOptions(stage_name='dev')
        )
        
        for function_name, info_dict in LAMBDA_CONFIG.items():
            folder_name = info_dict['folder']
            http_method = info_dict['http_method']
            timeout_duration = info_dict['timeout_duration']
            lambda_function = _lambda.Function(self, id=function_name, runtime = _lambda.Runtime.PYTHON_3_9,
                                        handler='{}.{}.lambda_handler'.format(folder_name, function_name),
                                        timeout= core.Duration.seconds(timeout_duration),
                                        code = _lambda.Code.from_asset('lambda', bundling={
                                            'image':core.DockerImage.from_registry("python:3.9"),
                                            'command': [
                                                "bash", "-c",
                                                "pip install --no-cache -r requirements.txt -t /asset-output && cp -au . /asset-output"
                                            ]
                                        }), role = lambda_role)

            if http_method:
                resource = api.root.add_resource(function_name)
                resource.add_method(http_method, _apigateway.LambdaIntegration(lambda_function))
