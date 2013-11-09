# -*- coding: utf-8 -*-
"""
Django heroku deployment settings for {{cookiecutter.project_name}} project.
"""


from .base import *


WSGI_APPLICATION = '{{cookiecutter.project_name}}.wsgi.heroku.application'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allowed host headers
# https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
# Allow all host headers
ALLOWED_HOSTS = ['*']
