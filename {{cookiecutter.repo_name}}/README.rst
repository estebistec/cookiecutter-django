{{cookiecutter.project_name}}
=============================

{{cookiecutter.description}}

LICENSE: MIT

Development
-----------

TODO

Deployment
----------

TODO

Environments
------------

PostgreSQL is the storage used in all environments.

base
~~~~

**Environment variables**

- **``DJANGO_SECRET_KEY``**

local
~~~~~

Expects a PostgreSQL database of the same name as the project.

**Environment variables**

- **``PGUSER``** - PostgreSQL user; **default**: current OS user
- **``PGPASS``** - PostgreSQL password; **default**: ``''``
