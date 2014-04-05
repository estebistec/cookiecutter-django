{{cookiecutter.project_name}}
=============================

{{cookiecutter.description}}

**TODO**

- Document your project, perhaps using `Sphinx <http://sphinx-doc.org/>`_.

License
-------

MIT

Environments
------------

Every environment must have at least the following components:

- a settings module
- a requirements file

Deployment environments may have further components, such as a Procfile and WSGI application.

**TODO**

- Define and document your environments. Local development and heroku are provided as examples.

**See:**

- https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
- https://docs.djangoproject.com/en/1.6/topics/settings/
- https://docs.djangoproject.com/en/1.6/ref/settings/

Development (local)
~~~~~~~~~~~~~~~~~~~

- **requirements**: ``requirements/dev.txt``
- **settings**: ``{{cookiecutter.project_name}}.settings.local``

**Tools**

- `bugjar <http://pybee.org/bugjar/>`_
- `cricket <http://pybee.org/cricket/>`_
- `django-debug-toolbar <http://django-debug-toolbar.readthedocs.org/>`_
- `docformatter <https://github.com/myint/docformatter>`_
- `duvet <http://pybee.org/duvet/>`_
- `Flake8 <https://flake8.readthedocs.org/en/2.0/>`_
- `pip-tools <https://github.com/nvie/pip-tools>`_
- `Pylint <http://www.pylint.org/>`_

**TODO**

- Specify ``SECRET_KEY`` as an environment variable (e.g., in a virtualenv postactivate).
- Specify ``DATABASE_URL`` as an environment variable (e.g., in a virtualenv postactivate).

Heroku
~~~~~~

- **requirements**: ``requirements/base_deploy.txt``
- **settings**: ``{{cookiecutter.project_name}}.settings.heroku``
- **wsgi app**: ``{{cookiecutter.project_name}}.wsgi.heroku.application``

**TODO**

- Email settings. See: https://docs.djangoproject.com/en/1.6/topics/email/
- Logging settings. See: https://docs.djangoproject.com/en/1.6/topics/logging/
- Create requirements.txt in the repo-root that references `requirements/base_deploy.txt`
- Define a procfile and deploy! See: https://devcenter.heroku.com/articles/getting-started-with-django
- Don't forget your secret: ``heroku config:add SECRET_KEY=s3cr3t`` (of course, use a good value)

Example `Procfile`::

    web: gunicorn {{cookiecutter.project_name}}.wsgi.heroku

Example `requirements.txt`::

    -r requirements/base_deploy.txt
