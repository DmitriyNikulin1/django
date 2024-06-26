FROM python:3.10-alpine

RUN apk update && \
    apk add nano

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk add gcc musl-dev linux-headers python3-dev
RUN pip install --upgrade pip setuptools
COPY ./req.txt /app
RUN pip install -r req.txt

EXPOSE 8000
