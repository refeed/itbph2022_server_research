#!/bin/sh

sudo apt install python3-pip -y
pip install -r requirements.txt

sysctl -w fs.file-max=500000
sysctl -p
