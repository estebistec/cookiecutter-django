# -*- coding: utf-8 -*-
"""
Django base settings for {{cookiecutter.project_name}} project.
"""


import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Use this to get required environment variables
def get_env_variable(var_name):
    """Get the named environment variable or raise ImproperlyConfigured"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = u"Missing the {} env variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{cookiecutter.project_name}}.urls'


# Databases specified with dj-database-url
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# https://github.com/kennethreitz/dj-database-url
# Examples:
# * dj_database_url.parse("sqlite:///{}".format(os.path.join(BASE_DIR, 'db.sqlite3')))
# * dj_database_url.parse("sqlite://:memory:")
# * dj_database_url.parse("postgresql://username:password@host:port/database")
# * dj_database_url.parse("mysql://username:password@host:port/database")
# * dj_database_url.config()  (use the DATABASE_URL environment variable)

DATABASES = {'default': dj_database_url.config()}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

