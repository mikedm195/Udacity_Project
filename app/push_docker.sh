make build
$(aws ecr get-login --no-include-email --region us-west-2)
docker tag fibonacci:latest 318180760014.dkr.ecr.us-west-2.amazonaws.com/udacity-project:latest
docker push 318180760014.dkr.ecr.us-west-2.amazonaws.com/udacity-project:latest