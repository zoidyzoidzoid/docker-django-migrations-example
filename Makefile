.PHONY: help
SHELL := /bin/bash

help:
	@echo 'We should add info about the commands here'

setup-dbs:
	@docker-compose down
	@docker-compose build
	@docker-compose rm -vf
	@docker-compose up -d db

fixtures: setup-dbs
	@echo '====Sleeping for 15s while DB initialises====' && sleep 15
	docker-compose run --rm web /usr/local/bin/python manage.py migrate
	@echo '====Done running migrations===='

up: fixtures
	-docker-compose up web
	@docker-compose down

bash: setup-dbs
	docker-compose run --service-ports --rm web bash

ps:
	docker-compose ps

