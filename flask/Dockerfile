FROM python:3.6.6-alpine3.8

RUN pip install -U pip
RUN apk update && apk upgrade

COPY run.sh /tmp/
CMD ["sh", "/tmp/run.sh"]