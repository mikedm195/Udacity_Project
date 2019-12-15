TEST ?= discover -s tests -p *Test*.py
IMAGE ?= fibonacci

build:
	docker-compose build

run:
	docker-compose -p $(IMAGE) up

test:
	# CMD="ls" docker-compose -p fibonacci up --build
	docker run --entrypoint=python3 $(IMAGE) -m unittest $(TEST) -v
	# CMD="python3 -m pytest -vv --cov=main $(TEST)" docker-compose -p fibonacci up 

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	docker run --entrypoint=hadolint $(IMAGE) Dockerfile
	docker run --entrypoint=pylint $(IMAGE) --disable=R,C,W1203 main.py
