FROM python:3.9-bullseye

RUN apt update &&\
    apt -y install nginx uwsgi

RUN mkdir -p /var/www/FreeMarketApi
WORKDIR /var/www/FreeMarketApi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

