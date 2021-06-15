1. Check if your template is valid

aws cloudformation validate-template --template-body <Template location ex. file://cfm/website.yaml> 

2. Create a stack - this step is required. Cloudformation will create your stack when it gets deployed.

aws cloudformation create-stack --stack-name < YOUR STACK NAME ex:s3websitestack> --template-body <Template location ex. file://cfm/website.yaml>

3. Deploy your stack 

aws cloudformation deploy --template-file <Template location ex. file://cfm/website.yaml> --stack-name <YOUR STACK NAME ex:s3websitestack > --s3-bucket cfmgsbucket

The last part is only required if a dedicated bucket being used to store stacks--s3-bucket cfmgsbucket

updating a template after uploading index and error html files

4. Upload index and error files and make them public

aws s3api put-object-acl --acl public-read --bucket <bucketname> --key error.html
aws s3api put-object-acl --acl public-read --bucket <bucketname> --key index.html
