import requests

#for people who are more relaxed
def relaxed_nonANA(longitude, latitude):
    KEY = "AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA"
    result = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude) + "&type=cafe&key=AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA&rankby=distance").json()

    #information that will be sent back to the client
    long_lat = (result['results'][0]['geometry']['location']['lng'], result['results'][0]['geometry']['location']['lat'])
    name = result['results'][0]['name']
    address = result['results'][0]['vicinity']

    return long_lat, name, address




print(relaxed_nonANA(-79.702870, 43.474928))
