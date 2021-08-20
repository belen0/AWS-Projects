## Creating a simple CodePipeline using CodeCommit as the source

Please note: You need to configure Git Credentials to connect with your CodeCommit repositories - [Setup Git Credentials](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html)
#### Deployment: 
* Create a repository and EC2 instance using CodeCommit [stack](https://github.com/gsidhu13/AWS-Projects/blob/main/CodeCommit_SimplePipeline/CodeCommit.yaml) and note output values - cloneurlhttp and DNS name 

   ***aws cloudformation create-stack --stack-name repocommit --template-body file://CodeCommit.yaml --capabilities CAPABILITY_NAMED_IAM*** 
 
* (No need if you already have the output value) Check the status of the stack and get output values:
   
   ***aws cloudformation describe-stacks --stack-name repocommit***
   
   Ex Output Value - *https://git-codecommit.us-east-1.amazonaws.com/v1/repos/mydemoRepo*

    
* Create a local folder and clone the repo

   git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/mydemoRepo 
   enter in git credentials username and password 
  
* Add sample.zip [folder](https://github.com/gsidhu13/AWS-Projects/blob/main/CodeCommit_SimplePipeline/SampleApp_Linux.zip) to the local folder and push the changes to the CodeCommit repository

* Create a CodePipeline using pipeline [stack](https://github.com/gsidhu13/AWS-Projects/blob/main/CodeCommit_SimplePipeline/Pipeline.yaml)

  ***aws cloudformation create-stack --stack-name pipeline --template-body file://Pipeline.yaml --capabilities CAPABILITY_NAMED_IAM***

* To test the entire setup - copy ***DNS Name*** output value from Step 1 and paste it in any web browser's address bar


How I planned this entire Project - [Planning](https://github.com/gsidhu13/AWS-Projects/blob/main/CodeCommit_SimplePipeline/Plan)
