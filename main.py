from flask import Flask,request,render_template, jsonify, redirect, url_for
import json
import os
from werkzeug.utils import secure_filename

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'instameeter-c5f6c6dac420.json'

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Shane!"

if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)