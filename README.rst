Yet Another Cookiecutter Django
===============================

A Django boilerplate powered by Cookiecutter_


Features
---------

* For Django 3.1
* Works with Python 3.6
* Python dependency management via Poetry_
* 12-Factor_ based settings via django-environ_
* Optimized development and production settings
* Media storage using Amazon S3 or Google Cloud Storage
* Docker support using docker-compose_ for development
* Procfile_ for deploying to Heroku

.. _`maintained Foundation fork`: https://github.com/Parbhat/cookiecutter-django-foundation


Optional Integrations
---------------------

*These features can be enabled during initial project setup.*

* Configuration for Celery_
* Configuration for Django Rest Framework (drf_)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _Poetry: https://python-poetry.org/
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Procfile: https://devcenter.heroku.com/articles/procfile
.. _Celery: http://www.celeryproject.org/
.. _docker-compose: https://github.com/docker/compose
.. _drf: https://www.django-rest-framework.org/


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using ``startproject``
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get Cookiecutter. Trust me, it's awesome::

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo::

    $ cookiecutter https://github.com/rmaceissoft/cookiecutter-django-ya

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

Answer the prompts with your own desired options.