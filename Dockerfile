FROM python:3.9-bullseye

RUN apt update &&\
apt -y install netcat &&\
rm -rf /var/apt/cache/*

WORKDIR /var/www/freemarketapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip3 install --no-cache -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /var/www/freemarketapi/entrypoint.sh

RUN useradd --no-create-home www_user
USER www_user

COPY . .

ENV ENV="/var/www/freemarketapi/.env"

ENTRYPOINT ["sh", "/var/www/freemarketapi/entrypoint.sh"]

