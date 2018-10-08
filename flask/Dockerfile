FROM python:3.6.6-alpine3.8

RUN pip install -U pip
RUN apk update && apk upgrade

WORKDIR /flask

COPY requirements.txt /flask

RUN pip install -r requirements.txt