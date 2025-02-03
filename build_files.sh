#!/bin/bash

# Start build
echo "BUILD START"

# Install dependencies
python -m pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# End build
echo "BUILD END"
