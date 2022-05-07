#!/bin/bash

cd ~/weblate
. .venv/bin/activate
python manage.py dbshell
