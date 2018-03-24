from www.config.production import *

CELERY_BROKER = CELERY_RESULT_BACKEND = 'redis://redis'

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 18000}

STATIC_ROOT = "/static"
MEDIA_ROOT = "/media"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 5000,
        }
    }
}

EMAIL_HOST = "smtp.ulb.ac.be"
SERVER_EMAIL = "dochub@urlab.be"

ADMINS = ('Nikita Marchant', "nikita.marchant@gmail.com")
MANAGERS = ADMINS
ALLOWED_HOSTS = ['dochub.be', '0.0.0.0', 'dochub.devel']

import raven
from os.path import dirname

BASE_DIR = dirname(dirname(dirname(__file__)))

# RAVEN_CONFIG = {
#     'dsn': 'https://80904abe5a184a78969d711801f016e2:e4233ed817d5416aa97ca9027723dc29@sentry.io/266326',
#     'release': raven.fetch_git_sha(BASE_DIR),
# }

# INSTALLED_APPS = INSTALLED_APPS + (
#     'raven.contrib.django.raven_compat',
# )

# SECRET_KEY = "yolo"


SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
