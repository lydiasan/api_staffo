#!/usr/bin/env python

from flask import Flask, render_template, request


main = Flask(__name__)

@main.route('/')
def login():
    return render_template('login.html')

@main.route('/', methods=['POST'])
def getvalue():
    subdomain = request.form['subdomain']
    email = request.form['email']
    password = request.form['password']
    print(subdomain)
    return render_template('request.py', subdomain=subdomain, email=email, password=password)

@main.route('/db')
def db():
    return render_template('db.html')
