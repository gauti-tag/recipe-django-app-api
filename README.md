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

## Generate Migrations for all define models
python manage.py makemigrations

## Applying Migrations
python manage.py migrate

## Command to create superuser
docker-compose run --rm app sh -c "python manage.py createsuperuser"
credentials: email: gautier.tiehoule@gmail.com password: Papatchi1994

## Install Auto API Documentation - DRF (Document Rest Framework)
library name: drf-spectacular

## Create User App
docker-compose run --rm app sh -c "python manage.py startapp user"
- remove migrations folder
- remove admin.py
- remove models.py
- remove tests.py
- create new folder 'tests'
- create new file '__init__.py' inside the 'tests' folder