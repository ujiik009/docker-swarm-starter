# app/routes.py: default route page
from app import app
import socket
from flask import Flask, request


@app.route('/')
@app.route('/index')
def index():
    return "Hello Flask World!"

@app.route('/healthcheck')
def healthcheck():
    return "hostname : "+socket.gethostname()

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)