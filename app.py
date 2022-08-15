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
    resp = make_response(render_template('index.html'))
    c.execute('''
        SELECT user_id FROM users WHERE user_id = ?
    ''', )
    resp.set_cookie('token', user)
    return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        message = request.form['username']
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')