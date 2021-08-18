#!/bin/sh

set -e # exit if errors happen anywhere

python3 -m venv venv
pip3 install -e .
sbase install chromedriver
apt-get update
apt-get install chromium -y
flask init-db
