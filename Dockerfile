FROM python:3.9-bullseye

RUN apt update &&\
apt -y install netcat &&\
rm -rf /var/apt/cache/*

RUN mkdir -p /var/www/freemarketapi
COPY . /var/www/freemarketapi
WORKDIR /var/www/freemarketapi

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
COPY ./manage.py .
COPY ./uwsgi.ini .

RUN mkdir -p /var/run/freemarket

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /var/www/freemarketapi/entrypoint.sh &&\
chmod +x /var/www/freemarketapi/entrypoint.sh

RUN useradd --no-create-home www_user
USER www_user

COPY . .

ENV ENV="/var/www/freemarketapi/.env"

ENTRYPOINT ["/var/www/freemarketapi/entrypoint.sh"]

