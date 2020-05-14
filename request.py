#!/usr/bin/env python

from pystaffo import StaffoAccount
import requests
import json
import app
from flask import Flask


app = Flask(__name__)

account = StaffoAccount(subdomain=subdomain, email=email, password=password)

account.get_location('Paris')

# will return all shifts for specified location
r = requests.get('https://api.github.com/user/locations/64/shifts.json', auth=('subdomain', 'email', 'password'))
data = json.dumps(r.json) # récupère les datas issues de la requête et en fait un tableau

if __name__ == "__main__":
    app.run()
