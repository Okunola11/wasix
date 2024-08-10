### DOCKER CLI COMMANDS

ENV_PATH=./.env

.PHONY: docker-run-all
docker-run-all:
	# stop and remove all running containers to avoid name conflicts

	# docker network create bp-network

	docker run -d \
		--name bp-api-dev \
		--network bp-network \
		--env-file=${ENV_PATH} \
		-v ./:/usr/src/ \
		-v venv:/usr/src/.venv:delegated \
		-p 7001:7001 \
		--restart unless-stopped \
		boilerplate:0


.PHONY: dokcer-start
docker-start:
	-docker start bp-api-dev
	-docker start test-db

.PHONY: docker-stop
docker-stop:
	-docker stop bp-api-dev

.PHONY: docker-rm
docker-rm:
	-docker container rm bp-api-dev
	# -docker network rm bp-network
	