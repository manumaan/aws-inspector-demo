# aws-inspector-demo
Demo for AWS Inspector

**Vulnerable EC2**
Older Debian (10) AMI to create vulnerable EC2:
```
https://aws.amazon.com/marketplace/pp/prodview-vh2uh3o4pdfow#pdp-overview
```

**Vulnerable Container image**
Check the mytestimage folder in repo to create the vulnerable docker image. The rar file is just some text files. Once the image is created, with say name mytestimage, upload to ECR. 

Steps to upload to ECR:
1. In AWS ECR create the repository called vuln-demo (or any other name)
2. Get the ECR repository URL. This looks like: 471112636280.dkr.ecr.us-east-1.amazonaws.com/vuln-demo
3. Login to the ECR from terminal (change the URL of ECR. Repo name is not needed at the end)
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 471112636280.dkr.ecr.us-east-1.amazonaws.com
```
5. Tag the local image with the name on ECR
```
docker tag mytestimage:0.1 471112636280.dkr.ecr.us-east-1.amazonaws.com/vuln-demo 
```
7. Upload the image
```
docker push 471112636280.dkr.ecr.us-east-1.amazonaws.com/vuln-demo:latest
```
   
**Vulnerable Lambda**
Check the nogood-lambda.py for a lambda that would trigger vulnerability findings. 
