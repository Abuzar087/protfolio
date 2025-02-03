#!/bin/bash

# Start build
echo "BUILD START"

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# End build
echo "BUILD END"
