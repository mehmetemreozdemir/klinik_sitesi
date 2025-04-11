#!/bin/bash
cd "$(dirname "$0")"/backend
source venv/bin/activate
python manage.py runserver &
sleep 3
open http://localhost:8000
wait