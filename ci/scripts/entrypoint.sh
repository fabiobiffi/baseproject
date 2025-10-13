#!/bin/bash

cd src/ &&
python manage.py collectstatic --noinput &&

# apply all migrations
python manage.py makemigrations &&
python manage.py migrate &&

# running all custom commands for project startup
echo "Running custom commands" &&
python manage.py createsuperuser --username admin --email admin@mail.com --noinput
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('Eow%pKECjz**w4oZ'); user.save()" &&

# starting cron service
systemctl enable cron &&
systemctl start cron &&

# running gunicorn
gunicorn baseproject.asgi:application -c baseproject/gunicorn.py
