from flask import *
import base64
import datetime
import random
import os

import sqlite3

conn = sqlite3.connect('pantherchat.db') 
c = conn.cursor()

def sqlexec(query):
    c.execute(query)

app = Flask(__name__)

allowedcharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
def checkallowedcharacters(username):
    for character in username:
        if not character in allowedcharacters:
            return False
    return True

configs = []
tokens = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form("email")
        userid = -1
        if '@' in username and '.' in username:
            userid = c.execute("SELECT user_id FROM users WHERE email = ?", username)
        elif checkallowedcharacters(username):
            token = os.urandom(20)
            while tokens[token] != 0:
                
            return redirect("feed.html")
        else:
            flash
        return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        resp = make_response(render_template("register.html"))
        message = request.form['username']

        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        resp.set_cookie('token', user)
        return resp
    else:
        return render_template('register.html')

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    return render_template("feed.html")

connection.close()
