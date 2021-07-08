#!/bin/bash
aws cloudformation --stack-name s3pipeline --template-body file://s3pipeline.yaml --parameters ParameterKey=KeyName, ParameterValue=ec2pipeline
aws s3api put-object --bucket s3pipelinegs --key aws/SampleApp_Windows.zip 