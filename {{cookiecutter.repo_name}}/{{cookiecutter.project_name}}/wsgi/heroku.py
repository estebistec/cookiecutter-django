# -*- coding: utf-8 -*-
"""
WSGI config for {{cookiecutter.project_name}} project Heroku deployment.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_name}}.settings.heroku")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply dj-static wsgi middleware
# https://github.com/kennethreitz/dj-static
from dj_static import Cling
application = Cling(application)
