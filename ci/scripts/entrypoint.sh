#!/bin/bash

cd src/ &&
python manage.py collectstatic --noinput &&

# apply all migrations
python manage.py migrate &&

# running all custom commands for project startup
echo "Running custom commands"

# starting cron service
systemctl enable cron &&
systemctl start cron &&

# running gunicorn
gunicorn baseproject.asgi:application -c baseproject/gunicorn.py
