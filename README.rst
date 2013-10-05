cookiecutter-django
===================

A cookiecutter template for Django websites. This is a very basic django project layout, started
using the django startproject command and then massaged into the layout prescribed by the book
`Two Scoops of Django <https://django.2scoops.org>`_.

This template will evolve from there, but this seems like a pretty good start

Project features
----------------

License
~~~~~~~

MIT

Runtime
~~~~~~~

- Django 1.5.4
- psycopg2
- PostgreSQL storage (tested against 9.3.0)

Django setup
~~~~~~~~~~~~

- admin site enabled
- clickjacking protection enabled
- sites framework disabled
- no user media settings
- local: django-debug-toolbar enabled
- local: streaming console logging enabled

Django add-ons
~~~~~~~~~~~~~~

- South
- Jinja for templates via django-jinja
- dj-static
- dj-database-url

Development tools
~~~~~~~~~~~~~~~~~

Note that these dependencies (see requirements/local.txt) are not pinned. The idea here is to
always take the latest releases for tools as they don't affect the project run-time.

* flake8
* docformatter
* pylint
* cricket
* bugjar
* duvet
