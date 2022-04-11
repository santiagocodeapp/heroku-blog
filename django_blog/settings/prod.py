from django_blog.settings.dev import ALLOWED_HOSTS, SECRET_KEY
import django_on_heroku
from decouple import config

from . base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'django-basic-blog.herokuapp.com'
]

