FROM python:3.9-bullseye

RUN apt update &&\
    apt -y install nginx uwsgi

RUN mkdir -p /var/www/freemarketapi
COPY . /var/www/freemarketapi
WORKDIR /var/www/freemarketapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
COPY ./manage.py .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

