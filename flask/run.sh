#! /bin/sh

cd /flask
pip install -r requirements.txt

cd /flask/api
flask run -h 0.0.0.0 -p 5000