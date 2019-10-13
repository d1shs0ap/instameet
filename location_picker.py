import requests

#for people who are more relaxed and non alchoholic anonymous
def relaxed_nonANA(longitude, latitude):
    KEY = "AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA"
    result = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude) + "&type=cafe&key=AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA&rankby=distance").json()

    #information that will be sent back to the client
    long_lat = (result['results'][0]['geometry']['location']['lng'], result['results'][0]['geometry']['location']['lat'])
    name = result['results'][0]['name']
    address = result['results'][0]['vicinity']

    return long_lat, name, address

#for people who are looking for quiet places.
def quiet_perfered(longitude, latitude):
    KEY = "AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA"
    result = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude) + "&type=library&key=AIzaSyDb4u5Xj_tfmHjfBx0ebKB_HiVaeqSGKLA&rankby=distance").json()
    
    long_lat = (result['results'][0]['geometry']['location']['lng'], result['results'][0]['geometry']['location']['lat'])
    name = result['results'][0]['name']
    address = result['results'][0]['vicinity']

    return long_lat, name, address
    



#def quiet_pref():





#print(relaxed_nonANA(-79.702870, 43.474928))
