#!/usr/bin/env python

from flask import Flask, render_template, request
import templates
import request


app = Flask(__name__)

#@app.route('/')
#def login():
#    return render_template('login.html')

@app.route('/', methods=['POST'])
def getvalue():
    subdomain = request.form['subdomain']
    email = request.form['email']
    password = request.form['password']
    return data

@app.route('/db')
def db():
    return render_template('db.html')

if __name__ == "__main__":
    app.run()
