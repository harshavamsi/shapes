import os

from shapes.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['shapes.org.in','localhost']

STATIC_ROOT = os.environ.get('STATIC_ROOT', None)