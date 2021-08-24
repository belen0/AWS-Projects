import boto3
import json 

# Boto3 Clients

iam = boto3.client('iam')
client = boto3.client('lambda')
rolename = 'lambda_role2'
inputbucket = 'inputbuckgs'

#Assume policy for role policy 

assumerolepolicy = {
        "Version": "2012-10-17",
        "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "lambda.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
        ]
    }

#Creating a role and adding assume role policy 

response_role = iam.create_role(
    RoleName= rolename,
    AssumeRolePolicyDocument= json.dumps(assumerolepolicy),                    
    Description='lambda function for role',
)

# generate role arn 
rolearn = response_role['Role']['Arn']
#Lambda Function

response_lam = client.create_function(
    FunctionName='transcoder-lambda',
    Runtime='python3.7',
    Role = rolearn ,
    Handler='index.handler',
    Code={
        'S3Bucket': inputbucket,
        'S3Key': 'function.zip'
    },
    Description='function to transcode videos'
)



