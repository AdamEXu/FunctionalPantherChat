from flask import *
import base64
import string
import random
import os
import waitress

app = Flask(__name__)

configs = []

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    print("Server Started!")
    waitress.serve(app, host="0.0.0.0", port=80) 
