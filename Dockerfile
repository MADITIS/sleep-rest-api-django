FROM bitnami/python:3.10.11
LABEL maintainer="manik das"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.dev.txt /requirements/requirements.dev.txt
COPY ./requirements.prod.txt /requirements/requirements.prod.txt

WORKDIR /app

COPY ./app .

ARG DEV=false

RUN apt-get update \
    && apt-get install -y postgresql-client \
                          build-essential \
                          libpq-dev && \
    if [ $DEV = "true" ]; \
        then pip install -r /requirements/requirements.dev.txt ; \
    fi && \
    pip install -r /requirements/requirements.prod.txt && \
    rm -rf /requirements && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static

EXPOSE $DJANGO_PORT

# python manage.py collectstatic
