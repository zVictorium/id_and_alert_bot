#!/bin/bash

NAME="Bot de Discord de DNI y alertas"
REPOSITORY="dni_and_alert_bot"

# GitHub
echo "(${NAME}) Preparing GitHub dependencies..."
cd "${REPOSITORY}"
git pull --force

# Python Packages
echo "(${NAME}) Preparing Python dependencies..."
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt