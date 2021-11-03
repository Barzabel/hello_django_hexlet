install: #poetry install
	poetry install;

run-server: 
	poetry run python manage.py runserver

run-server-gunicorn:
	export DJANGO_SETTINGS_MODULE=hello_django.settings
	poetry run gunicorn hello_django.wsgi

console:
	poetry run python django-admin shell