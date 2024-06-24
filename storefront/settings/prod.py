import os
from .common import *


DEBUG = False

SECRET_KEY = 'fxb@ctrddm4$sx8=-2@i!s426_l1+=7=okml6*f+iwfy&4_3f7'

ALLOWED_HOSTS = ['158.160.139.142']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'PostgreSQL-1066',
        'HOST': '83.166.234.62',
        'USER': 'user',
        'PASSWORD': 'Agent2008Agent2008!',
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
