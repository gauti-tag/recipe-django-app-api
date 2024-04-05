# recipe-django-app-api
Recipe API Project using Django, Docker, Docker-compose, PostgreSQL

## run and test flake8
docker-compose run --rm app sh -c "flake8"

## Create django app
docker-compose run --rm app sh -c "django-admin startproject app ."