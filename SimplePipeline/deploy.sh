#!/bin/bash
aws cloudformation --stack-name s3pipeline --template-body file://<your folder>/s3pipeline.yaml --parameters ParameterKey=KeyName, ParameterValue=ec2pipeline
aws s3api put-object --bucket s3pipelinegs --key <your folder>/SampleApp_Windows.zip 
