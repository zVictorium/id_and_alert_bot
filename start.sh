#!/bin/bash

NAME="Bot de Discord de DNI y alertas"
REPOSITORY="dni_and_alert_bot"

# Start script
echo "(${NAME}) Starting script..."
cd "${REPOSITORY}"
source venv/bin/activate
python main.py