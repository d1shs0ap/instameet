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
    from optimize_point import geometric_median
    firebase_call = requests.get("https://instameet-87f5c.firebaseio.com/.json").json()

    #list of longitudes and latitudes
    long_and_lat = []
    for i in firebase_call:
        long_and_lat.append([firebase_call[i]["Longitude"], firebase_call[i]["Latitude"]])
    #checking if there are enough datasets in the database
    if len(firebase_call) <= 4:
        print(geometric_median(long_and_lat))
    else:
        print(geometric_median(long_and_lat))
        
    #origin = "University of Toronto"
    #destination = "Scotia Bank Plaza"
    #google_result = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&key=AIzaSyCHttcfy83akWGX0yXCX53DnrVN1anZFEM&alternatives=true").json()
    return firebase_call

if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)