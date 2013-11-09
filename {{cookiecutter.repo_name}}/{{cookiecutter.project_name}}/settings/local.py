# -*- coding: utf-8 -*-
"""
Django quick-start development settings for {{cookiecutter.project_name}} project.

"""


from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True


ALLOWED_HOSTS = []


# Email console backend for development
# https://docs.djangoproject.com/en/1.6/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Logging
# https://docs.djangoproject.com/en/1.6/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


# Django Debug Toolbar
# http://django-debug-toolbar.readthedocs.org/

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}
