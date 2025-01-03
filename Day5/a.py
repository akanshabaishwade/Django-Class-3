'''
Starting a project:

* You can start a new Django project using the django-admin command. For example, django-admin startproject myproject creates a new Django project called "myproject". This command creates a directory structure with files for settings, URLs, and the project's main Python package.

Difference between an App and a Project:

* In Django, a project is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings. It represents a complete web application.
* A project is typically the top-level directory that contains all the files and directories needed for a Django application to run.
* a project's default file names include settings.py (for project settings), urls.py (for URL patterns), wsgi.py (for WSGI deployment), asgi.py (for ASGI deployment), manage.py (for project management)
* An application is typically designed to serve a specific purpose or feature within a project, and can include models, views, templates, and static files.
* In a Django app, the default file names include init.py (for package recognition), models.py (for database models), views.py (for view functions), admin.py (for admin interface registration), and apps.py (for app configuration).


how to create django project:-
django-admin startproject myproject
django-admin startproject myproject .

'''