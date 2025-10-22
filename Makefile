export DOCKER_DEFAULT_PLATFORM=linux/amd64
COMPOSE_DEV=docker-compose.yml

# DOCKER TASKS
dev-up: dev-down ## Spin up compose
	docker compose -f ${COMPOSE_DEV} up -d

dev-up-build: dev-down  ## Build and spin up compose
	docker compose -f ${COMPOSE_DEV} down
	docker compose -f ${COMPOSE_DEV} up --build

dev-down: ## Spin down compose
	docker compose -f ${COMPOSE_DEV} down

clean: dev-down ## Clean all docker images
	docker system prune -a --volumes -f