

#!/bin/bash

echo "BUILD START"

# Install dependencies
python3.11 -m pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput --clear

# Apply migrations
python3.11 manage.py migrate
 
echo "BUILD END"
