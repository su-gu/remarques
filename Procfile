release: cd remarques && python manage.py migrate
web: bash -c "cd remarques && gunicorn remarques.wsgi --log-file -"