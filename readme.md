# Phone Book API

[![Docker](https://img.shields.io/badge/docker-blue?logo=docker)](https://www.docker.com/)
[![Django](https://img.shields.io/badge/django-blue?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/python-blue?logo=python)](https://www.python.org/)
[![Django Rest Framework](https://img.shields.io/badge/django%20rest%20framework-blue)](https://www.django-rest-framework.org/)
[![Swagger](https://img.shields.io/badge/swagger-green?logo=swagger)](https://swagger.io/)

Phone book api to create, search, report user.

## Technologies Used

- Docker
- Django
- Python
- Django Rest Framework
- Swagger

## Installation and Setup

1. Install docker:
2. Build docker-compose
   ```shell
   docker-compose build
3. (optional)
    ```
    docker-compose run --rm api sh -c "python manage.py makemigrations && python manage.py migrate"
4. Run docker-compose
    ```shell
    docker-compose up

# Issues?
- OperationalError
    - This could happen because of the database race condition on the first run
    - To fix this re run the docker compose