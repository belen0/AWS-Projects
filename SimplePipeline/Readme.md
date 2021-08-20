## Creating a simple CodePipeline using S3 and EC2 

Please note this is one of the tutorials in AWS CodePipeline user guide — [Simple Pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-simple-s3.html) BUT I created the entire project using CloudFormation and deployed using AWS CLI

Deployment:
* (Optional) Create a key pair for your instance - [KeyPair](https://github.com/gsidhu13/AWS-Projects/blob/main/SimplePipeline/keyName)
* Provision all your resources using CloudFormation - [Template](https://github.com/gsidhu13/AWS-Projects/blob/main/SimplePipeline/s3pipeline.YAML)
* Deploy your CFN stack and upload zip folder to your instance - [Deploy](https://github.com/gsidhu13/AWS-Projects/blob/main/SimplePipeline/deploy.sh)

I have this additional [Planning](https://github.com/gsidhu13/AWS-Projects/blob/main/SimplePipeline/Planning) file in here. This just suggests how I plan before I provisioned the resources for a stack. 

