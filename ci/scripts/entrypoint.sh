#!/bin/bash

cd src/ &&
uv run python manage.py collectstatic --noinput &&

# apply all migrations
uv run python manage.py makemigrations &&
uv run python manage.py migrate &&

# running all custom commands for project startup
echo "Running custom commands" &&
uv run python manage.py createsuperuser --username admin --email admin@mail.com --noinput
uv run python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('password'); user.save()" &&

# starting cron service
systemctl enable cron &&
systemctl start cron &&

# running gunicorn
uv run gunicorn baseproject.asgi:application -c baseproject/gunicorn.py
