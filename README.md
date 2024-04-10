# GitHub link
https://github.com/LondonAppDeveloper/c2-recipe-app-api-2

# recipe-django-app-api
Recipe API Project using Django, Docker, Docker-compose, PostgreSQL

## run and test flake8
docker-compose run --rm app sh -c "flake8"

## Create django app
docker-compose run --rm app sh -c "django-admin startproject app ."

## Run unit test on django app
docker-compose run --rm app sh -c "python manage.py test"

## Create a core app
docker-compose run --rm app sh -c "python manage.py startapp core"
remove tests.py and views.py files