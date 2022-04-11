from cgitb import handler
from django_blog.settings.dev import ALLOWED_HOSTS, SECRET_KEY
import django_on_heroku
from decouple import config

from . base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'django-basic-blog.herokuapp.com'
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datemt': "%d/%b/ %Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handler': ['console'],
            'level': 'DEBUG'
        },
    }
}

# Heroku settings

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
