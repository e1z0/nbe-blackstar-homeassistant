all: build

build:
	docker build -t nbe:latest -f docker/Dockerfile --no-cache=true .
build_aarch64:
	docker build -t nbe:aarch64 -f docker/Dockerfile --no-cache=true .
upload_aarch64:
	docker tag nbe:aarch64 nulldevil/nbe:aarch64
	docker push nulldevil/nbe:aarch64
upload:
	docker tag nbe:latest nulldevil/nbe:latest
	docker push nulldevil/nbe:latest
up:
	COMPOSE_PROJECT_NAME=nbe COMPOSE_IGNORE_ORPHANS=True docker-compose -f docker-compose.yml up -d
down:
	COMPOSE_PROJECT_NAME=nbe COMPOSE_IGNORE_ORPHANS=True docker-compose -f docker-compose.yml down
