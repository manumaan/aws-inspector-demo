# aws-inspector-demo
Demo for AWS Inspector


Older Debian (10) AMI to create vulnerable EC2:
```
https://aws.amazon.com/marketplace/pp/prodview-vh2uh3o4pdfow#pdp-overview
```

Check the Dockerfile in repo to create the vulnerable docker image. 

Check the nogood-lambda.py for a lambda that would trigger vulnerability findings. 
