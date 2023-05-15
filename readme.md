# Sleep Rest API
![Version](https://img.shields.io/badge/version-0.0.1--beta-orange)

![Django](https://img.shields.io/badge/Django-orange?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker)
[![Docker](https://img.shields.io/badge/docker-blue?logo=docker)](https://www.docker.com/)



[![Django Rest Framework](https://img.shields.io/badge/django%20rest%20framework-blue)](https://www.django-rest-framework.org/)


Sleep rest api-Beta

## Technologies Used

- Docker
- Django
- Python
- Django Rest Framework

## Installation and Setup

1. Configure the .env file
2. Install docker:
3. Build docker-compose
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
