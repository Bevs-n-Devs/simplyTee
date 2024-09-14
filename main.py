import os
from flask import Flask, render_template, url_for
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()                   # environment variables

app = Flask(__name__)           # config Flask app
CORS(app)                       # extra layer of protection

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(
        debug=True
    )