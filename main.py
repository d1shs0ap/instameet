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

    #checking if there are enough datasets in the database
    number_of_true = 0
    for i in firebase_call:
        if firebase_call[i]['Status'] == "True":
            number_of_true += 1

    #list of longitudes and latitudes
    long_and_lat = []
    for i in firebase_call:
        long_and_lat.append([firebase_call[i]["Longitude"], firebase_call[i]["Latitude"]])
    
    if number_of_people > number_of_true:
        #print(geometric_median(long_and_lat))
        return ('', 204)
    else:
        median = geometric_median(long_and_lat)
        median = (median[0], median[1])

        #the final location for where the people should meet
        #print(median, final_long_lat, name, address)
        final_long_lat, name, address = location_picker.relaxed_nonANA(median[0], median[1])

        #updated the database
        for i in firebase_call:
            UPDATE = requests.patch("https://instameet-87f5c.firebaseio.com/" + i + "/.json", json.dumps({"Status": "False"}))
        return jsonify({"final_long_lat": final_long_lat, 'name': name, 'address':address})

@app.route("/postresponse", methods=["POST"])
def postresponse():
    from sentimentanalysis import analyze_sentiment
    userfeedback = request.get_json(force=True)['userfeedback'] #gets json file from being post requested
    result = analyze_sentiment(userfeedback)

    #id = request.get_json(force=True)['id'] #this is the id of the user we want to add the feedback data to
    id = "27754"
    idnum = -1

    firebase_call = requests.get("https://instameet-87f5c.firebaseio.com/.json").json()

    for i, k in enumerate(firebase_call):
        if (k==id):
            idnum = i



    firebase_call = requests.get("https://instameet-87f5c.firebaseio.com/.json").json()

    #check which number id is in the list

    # getting the sentiments
    newSentiments = firebase_call[list(firebase_call.keys())[idnum]]['Sentiments']
    newSentiments.append(result)

    UPDATE = requests.patch("https://instameet-87f5c.firebaseio.com/"+id+"/.json", json.dumps({"Sentiments": newSentiments}))

    return jsonify({"score": result})


if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)
