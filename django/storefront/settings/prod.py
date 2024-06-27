import os
from .common import *


DEBUG = False

SECRET_KEY = 'fxb@ctrddm4$sx8=-2@i!s426_l1+=7=okml6*f+iwfy&4_3f7'


ALLOWED_HOSTS = ['158.160.140.159', 'django']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'pgdb',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.0.1.97:6379/0",
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
