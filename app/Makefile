TEST ?= discover -s tests -p *Test*.py

build:
	docker-compose build

run:
	docker-compose -p fibonacci up

test:
	# CMD="ls" docker-compose -p fibonacci up --build
	CMD="python3 -m unittest $(TEST) -v" docker-compose -p fibonacci up
	# CMD="python3 -m pytest -vv --cov=main $(TEST)" docker-compose -p fibonacci up 

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	hadolint Dockerfile
	pylint --disable=R,C,W1203 main.py
