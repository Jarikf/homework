import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = '*'
CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    # Frontend url for localhost development.
    'http://localhost:3000',
    'http://0.0.0.0:3000',
    # Swagger.
    'http://localhost:8000',
    'http://0.0.0.0:8000',
]
LOGLEVEL = 'DEBUG'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     os.environ['POSTGRES_DB'],
        'USER':     os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST':     os.environ['DJANGO_DB_HOST'],
        'PORT':     os.environ['DJANGO_DB_PORT']
    }
}

Q_CLUSTER = {
    'name': 'default',
    'workers': 1,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'catch_up': False,
    'redis': {
        'host': os.environ['REDIS_HOST'],
        'port': os.environ['REDIS_PORT'],
        'db': 0,
        'password': None,
        'socket_timeout': None,
        'charset': 'utf-8',
        'errors': 'strict',
        'unix_socket_path': None
    }
}


SWAGGER_AVAILABLE = True
SWAGGER_BASE_URL = 'http://localhost:8000'
