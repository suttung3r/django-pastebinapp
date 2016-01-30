=====
Pastebinapp
=====

Pastebinapp is a django-based based bin app with compilation built in.

Quick start
-----------

1. Add "pastebinapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'pastebinapp',
    ]

2. Include the pastebinapp URLconf in your project urls.py like this::

    url(r'^pastebinapp/', include('pastebinapp.urls')),

3. Run `python manage.py migrate` to create the pastebinapp models.

4. Start the development server and visit http://127.0.0.1:8000/pastebinapp.
   There is a link here to enter a new code snippet. Links to the latest
   snippets will also be displayed.
