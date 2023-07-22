from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3ld7_#pnw^_fu#op941j5kjuo4(wvsk@xs%p%c&ua5is#3&ocd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass