## Creating a Website using S3 bucket on AWS and domain that's register on Route 53


Please note: Domain was purchased before I started this project. If you need to register a domain, here are the instructions on [AWS Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)

How the setup looks like - [Design](https://github.com/gsidhu13/Projects/blob/d3825147780f757a5bbe5437ce67c74cb0c54cfa/WebsiteUsingS3&Route53/setup_pic.png)

Files that are required for a basic website — [Index](https://github.com/gsidhu13/Projects/blob/47373010cc05f0752b6a4512b79de1c6927708fb/WebsiteUsingS3&Route53/index.html) and [error](https://github.com/gsidhu13/Projects/blob/d3f515eb58e9d849f3dd735b78b4a44e03923410/WebsiteUsingS3&Route53/error.html) 

Cloudformation template to create s3 and route 53 resources —[Template](https://github.com/gsidhu13/Projects/blob/23271ec5bb9f5ac00c2b86c894fd4d8e6d97ae0a/WebsiteUsingS3&Route53/website.yaml) 

Cli [Commands](https://github.com/gsidhu13/Projects/blob/7075122ead36f19cbc2079f0f3d26d309111710c/WebsiteUsingS3&Route53/Cli_commands.md) to deploy the template and upload index and error files. 
