from flask import Flask,request,render_template, jsonify, redirect, url_for
import json
import requests
import os
from werkzeug.utils import secure_filename

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'instameeter-c5f6c6dac420.json'

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Shane!"

@app.route("/response", methods=["POST"])
def response():
    firebase_call = requests.get("https://instameet-87f5c.firebaseio.com/.json").json()
    origin = "University of Toronto"
    destination = "Scotia Bank Plaza"
    google_result = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&key=AIzaSyCHttcfy83akWGX0yXCX53DnrVN1anZFEM&alternatives=true").json()
    return firebase_call

if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)