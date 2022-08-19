from flask import *
import base64
import datetime
import string
import random
import os

import sqlite3

conn = sqlite3.connect('pantherchat.db') 
c = conn.cursor()

def sqlexec(query):
    c.execute(query)

app = Flask(__name__)

allowedcharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
        unencpw = request.form("password")
        random.seed(unencpw)
        encryptedpw = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
        random.seed(int(datetime.time.utc_now()))
        userid = -1
        if '@' in username and '.' in username:
            userid = c.execute("SELECT user_id FROM users WHERE email = ?", username)
        else:
            userid = c.execute("SELECT user_id FROM users WHERE username = ?", username)
        if checkallowedcharacters(username) and userid != -1:
            # Get password from sql database
            password = c.execute("SELECT password FROM users WHERE userid = ?", userid)
            if True:
                token = os.urandom(20)
                while tokens[token] != 0:
                    token = os.urandom(20)
                return redirect("feed.html")
        else:
            flash "Invalid account"
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
