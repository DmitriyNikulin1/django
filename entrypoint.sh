#!/bin/sh

python manage.py migrate
python manage.py collectstatic

gunicorn storefront.wsgi --bind 0.0.0.0:8000