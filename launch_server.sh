#!/bin/sh

pip install -r requirements.txt

cpu_number=$1
worker=$(expr $cpu_number \* 2)

gunicorn -w $worker server_dummy:app -b 0.0.0.0
