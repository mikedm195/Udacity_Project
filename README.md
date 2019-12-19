# Udacity_Project

## Infrastructure

To create the infrastructure and install kubernetes and jenkins:

Create a key pair in AWS and replace your key in the `kubernetes_cluster/cloudformation/kubernetes_infrastructure.yaml`
Replace your AWS credentials in `kubernetes_cluster/ansible/aws-credentials.yml` file.

>$ sh kubernetes_cluster/cloudformation/create.sh udacity_deployment kubernetes_infrastructure.yaml parameters.json

This will create 4 EC2 instances, one for kubernetes master, two for kubernetes workers and one for Jenkins

Copy the EC2 IPs and replace `kubernetes_cluster/ansible/hosts` with the corresponding IP

>$ sh kubernetes_cluster/ansible create.sh

This will install Kubernetes and Jenkins in their respective EC2 instance

## Code

Flask microservice for generating fibonacci numbers
We use docker compose to run code locally

>$ cd app/

### Build code

>$ make build

### Run local code

>$ make run

### Run unit tests

>$ make test

### Run lint

>$ make lint