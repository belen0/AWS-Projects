import boto3
import json 

inputbucket = 'inputbuckgs'
outputbucket = 'outputbucketgs'
thumbbucket = 'thumbnailbucketgs'
rolename = 'pipelinerole'
transcoder = boto3.client('elastictranscoder')
buckets = boto3.client('s3')
iam = boto3.client('iam')
client = boto3.client('lambda')
assumerolepolicy = {
        "Version": "2008-10-17",
        "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "elastictranscoder.amazonaws.com",
                                    "lambda.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
        ]
    }


response_role = iam.create_role(
    RoleName= rolename,
    AssumeRolePolicyDocument= json.dumps(assumerolepolicy),
                    
    Description='role created for transcoder pipeline',
)

rolearn = response_role['Role']['Arn']

#Create Policies
basicexecutiondocument = {

    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:us-east-1:4606749:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:4600049:log-group:/aws/lambda/transcoderfunction:*"
            ]
        }
    ]
}
policy1 = iam.create_policy(
  PolicyName='basicexecutionPolicy30',
  PolicyDocument=json.dumps(basicexecutiondocument)
)
ElasticTranscoderdocument = {
    "Version": "2012-10-17",
    "Statement": [
    {
        "Action": [
            "elastictranscoder:*",
            "s3:ListAllMyBuckets",
            "s3:ListBucket",
            "iam:ListRoles",
            "sns:ListTopics"
        ],
        "Effect": "Allow",
        "Resource": "*"
    },
    {
        "Action": [
            "iam:PassRole"
        ],
        "Effect": "Allow",
        "Resource": "*",
        "Condition": {
            "StringLike": {
                "iam:PassedToService": [
                    "elastictranscoder.amazonaws.com"
                ]
            }
        }
    }
    ]
}
policy2 = iam.create_policy(
  PolicyName='ElasticTranscoderPolicy30',
  PolicyDocument=json.dumps(ElasticTranscoderdocument)
)

S3FullPermissionsdocument = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
policy3 = iam.create_policy(
  PolicyName='S3FullPermissions30',
  PolicyDocument=json.dumps(ElasticTranscoderdocument)
)

ElastictranscodeputDocument= {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Action": [
                "s3:Put*",
                "s3:ListBucket",
                "s3:*MultipartUpload*",
                "s3:Get*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "2",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "*"
        },
        {
            "Sid": "3",
            "Effect": "Deny",
            "Action": [
                "s3:*Delete*",
                "s3:*Policy*",
                "sns:*Remove*",
                "sns:*Delete*",
                "sns:*Permission*"
            ],
            "Resource": "*"
        }
    ]
}

policy4 = iam.create_policy(
  PolicyName='Elastictranscoderpoli30',
  PolicyDocument=json.dumps(ElastictranscodeputDocument)
)
#Get Policies 

policy1arn = policy1['Policy']['Arn']
policy2arn = policy2['Policy']['Arn']
policy3arn = policy3['Policy']['Arn']
policy4arn = policy4['Policy']['Arn']

#Attach policies

attach1 = iam.attach_role_policy(
    PolicyArn=policy1arn,
    RoleName=rolename
)
attach2 = iam.attach_role_policy(
    PolicyArn=policy2arn,
    RoleName=rolename
)
attach3 = iam.attach_role_policy(
    PolicyArn=policy3arn,
    RoleName=rolename
)
attach4 = iam.attach_role_policy(
    PolicyArn=policy4arn,
    RoleName=rolename
)
bucket1 = buckets.create_bucket(
    ACL='private',
    Bucket= inputbucket,
)

print(bucket1)

response = buckets.create_bucket(
    ACL='private',
    Bucket= outputbucket,
)

response = buckets.create_bucket(
    ACL='private',
    Bucket= thumbbucket,
)
response = transcoder.create_pipeline(
    Name='transcodingvideo',
    InputBucket= inputbucket,
    Role=rolearn,
    ContentConfig={
        'Bucket': outputbucket,
        'StorageClass': 'Standard' },
    ThumbnailConfig={
        'Bucket': thumbbucket,
        'StorageClass': 'Standard', #Standard or ReducedRedundancy
    }
)



#Lambda Function

response_lam = client.create_function(
    FunctionName='transcoder-lambda',
    Runtime='python3.8',
    Role=rolearn,
    Handler='index.handler',
    Code={
        'S3Bucket': inputbucket,
        'S3Key': 'function.zip'
    },
    Description='function to transcode videos'
)


