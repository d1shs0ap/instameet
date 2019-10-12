from flask import Flask,request, jsonify
import json
import requests
import os
from werkzeug.utils import secure_filename

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'instameeter-c5f6c6dac420.json'

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Shane!"

@app.route("/preresponse", methods=["POST"])
def preresponse():
    from optimize_point import geometric_median
    import location_picker
    firebase_call = requests.get("https://instameet-87f5c.firebaseio.com/.json").json()

    #getting the number of people who are going to be at the site
    number_of_people = firebase_call[list(firebase_call.keys())[0]]['NumberOfPeople']

    #list of longitudes and latitudes
    long_and_lat = []
    for i in firebase_call:
        long_and_lat.append([firebase_call[i]["Longitude"], firebase_call[i]["Latitude"]])

    #checking if there are enough datasets in the database
    if len(firebase_call) < 4:
        #print(geometric_median(long_and_lat))
        pass
    else:
        median = geometric_median(long_and_lat)
    median = (median[0], median[1])

    #the final location for where the people should meet
    final_long_lat, name, address = location_picker.relaxed_nonANA(median[0], median[1])

    #print(median, final_long_lat, name, address)
    #checking the number of people
    return jsonify({"final_long_lat": final_long_lat, 'name': name, 'address':address})

@app.route("/postresponse", methods=["POST"])
def postresponse():
    from sentimentanalysis import analyze_sentiment
    userfeedback = request.get_json(force=True)['userfeedback'] #gets json file from being post requested
    result = analyze_sentiment(userfeedback)
    print(result)
    return jsonify({"score": result})


if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)