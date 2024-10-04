#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create a superuser if environment variables are set
if [ "$CREATE_SUPERUSER" = "true" ]; then
    python manage.py createsu
fi