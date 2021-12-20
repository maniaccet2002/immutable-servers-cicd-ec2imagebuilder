# immutable-servers-cicd-ec2imagebuilder
## Overview
This project provides cloudformation templates to automate the AMI creation for immutable EC2 instances using CICD pipeline and EC2 image builder. The CICD pipeline use a lambda function to trigger instance refresh on the  autoscaling groups to automate the deployment of the new AMI.

### EC2 Image Builder
EC2 Image Builder simplifies the building, testing, and deployment of Virtual Machine and container images for use on AWS or on-premises.With Image Builder, there are no manual steps for updating an image nor do you have to build your own automation pipeline. Refer https://aws.amazon.com/image-builder/ for mode information on EC2 image builder

### Instance Refresh on Auto Scaling group
When you are using Immuatable approach for the application infrastructure, a new AMI will be created for each and every application refresh and rolling out new EC2 instances using this new AMI. For AutoScaling groups, a new version of launch template needs to be created with the new AMI. Any new instance launched by the autoscaling group will use the new AMI but it does not terminate the existing instances. You can use Instance refresh feature available for auto scaling groups to initiate the process of replacing the existing instances with new ones. Refer https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html for more information on Instance Refresh feature.

## Architecture
Sample web application used for this project runs on an autoscaling group behind an application load balancer

Architecture of the CICD pipeline which automates the AMI creation 

### Pre requisutes
AWS Account 
AWS User with CLI access and sufficient permissions to create VPC, subnets, Load balancer, autoscaling group, CICD pipeline and execute cloudformation templates

### How to deploy the cloudformation template
#### Stack Creation
Download the template and application source code from the github repo
cd immutable-servers-cicd-ec2imagebuilder
execute the below command to create the stack
aws cloudformation create-stack --stack-name ec2imagebuilder --capabilities CAPABILITY_NAMED_IAM --template-body file://template.yml
Login to AWS console and navigate to cloudformation. Check the status of the cloudformation template execution and wait till the stack gets created successfully

#### Initiate CICD pipeline
Once the stack gets created successfully, we need to check in the application package on to the code commit repository. Application package contains buildspec.yml file which will be used by the code build stage as well as imagebuilder.yml which contains the cloudformation template used to create the new AMI using EC2 image builder
Execute the below steps to check in the source code to code commit repository

git clone <HTTPS URL of the repository> (check cloudformation Outputs section from the previous step for the repository URL)
cd ec2imagebuilder-source
copy the contents of the source folder from the previous step. Command: cp -rf <immutable-servers-cicd-ec2imagebuilder>/source/* .
git add .
git commit -m 'Application Code'
git push
when prompted, enter the code commit crednetials of the user. Refer the below link to generate the code commit credentials for your user

https://aws.amazon.com/blogs/devops/introducing-git-credentials-a-simple-way-to-connect-to-aws-codecommit-repositories-using-a-static-user-name-and-password/


Monitor the status of the code pipe execution from the AWS console. Once the pipeline execution is completed, you will be able to access the application(Refer cloudformation Outputs section for the application URL )
test
