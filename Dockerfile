FROM python:3.10-alpine

RUN apk update && \
    apk add nano

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./django /app
WORKDIR /app

RUN apk add gcc musl-dev linux-headers python3-dev
RUN pip install --upgrade pip setuptools
COPY ./req.txt /app
RUN pip install -r req.txt
RUN apk add py3-gunicorn

EXPOSE 8000

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]


