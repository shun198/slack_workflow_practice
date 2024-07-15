APP_CONTAINER_NAME=app
RUN_APP = docker-compose exec $(APP_CONTAINER_NAME)
RUN_POETRY =  $(RUN_APP) poetry run

prepare:
	docker-compose up -d --build

up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .
