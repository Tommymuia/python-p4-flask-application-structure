#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome to my page!<h1>'

# append to server/app.py
@app.route('/<username>')
def user(username):
    return f'<h1>Profile picture for {username}</h1>'

# modify user() in server/app.py
@app.route('/<string:username>')
def user_list(username):
    return f'Profile picture for {username}'

if __name__ =='__main__':
    app.run(port=5555,debug=True)