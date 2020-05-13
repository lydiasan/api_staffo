#!/usr/bin/env python

import pystaffo
import requests
import json
import main
from flask import Flask


app = Flask(__name__)

account = StaffoAccount(subdomain=subdomain, email=email, password=password)

account.get_location('Paris')

# will return all shifts for specified location
r = requests.get('https://api.github.com/user/locations/64/shifts.json', auth=('subdomain', 'email', 'password'))
return r

if __name__ == "__main__":
app.run()
