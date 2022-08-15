from flask import *
import base64
import datetime
import random

import sqlite3

conn = sqlite3.connect('pantherchat.db') 
c = conn.cursor()

app = Flask(__name__)

configs = []
tokens = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        message = request.form['username']

        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        resp.set_cookie('token', user)
        return resp
    else:
        return render_template('login.html')