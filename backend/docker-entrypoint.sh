#!/bin/sh
handle_error() {
    echo "An error occurred on line $1"
    exit 1
}

trap 'handle_error $LINENO' ERR

echo "Waiting for postgres..."

while ! nc -z "postgres" "5432"; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py migrate --no-input
python manage.py seed_cache_after_fixtures
gunicorn "backend.wsgi:application" --bind 0.0.0.0:5000