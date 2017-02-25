"""
backend.py

Author: Jeremiah Lantzer

Travel reccomendations on a budget.

Insta Auth Token Jeremiah: 42404802.114b636.262414e1e9324e88a8d1de70562b3039
Insta Auth Token Kelly: 22220287.114b636.9b53377e1cb84493a59a7950b16795bd
"""

import requests
import json
import re
from geopy.geocoders import Nominatim
from clarifai.rest import ClarifaiApp

payload = {'access_token': '42404802.114b636.262414e1e9324e88a8d1de70562b3039'}


# receives hashtags from liked photos
def getHashtags():
    hashtags = []
    r = requests.get('https://api.instagram.com/v1/users/self/media/liked', params=payload)
    jsonifier = json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))

    # Uncomment to view the data received from the request
    # print(jsonifier)

    for x in range(20):
        json_data = json.loads(jsonifier)
        caption = json_data["data"][x]["caption"]["text"]
        # print(caption)
        caption = str(caption)
        hashtags.append(re.findall(r"#(\w+)", caption))

    print(hashtags)
    return hashtags


def getLocations():
    places = []
    geolocator = Nominatim()
    r = requests.get('https://api.instagram.com/v1/users/self/media/liked', params=payload)
    jsonifier = json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    # print(jsonifier)

    for x in range(20):
        json_data = json.loads(jsonifier)
        try:
            latitude = json_data["data"][x]["location"]["latitude"]
            longitude = json_data["data"][x]["location"]["longitude"]
            # print(latitude)
            # print(longitude)
            lat_long = "%f, %f" % (latitude, longitude)
            location = geolocator.reverse(lat_long)
            raw = location.raw
            # print(raw)
            rawJson = json.dumps(raw, sort_keys=True, indent=4, separators=(',', ': '))
            raw_json = json.loads(rawJson)
            state = raw_json["address"]["state"]
            places.append(state)
            # print(state)
            try:
                city = raw_json["address"]["city"]
                places.append(city)
                # print(city)
            except KeyError:
                # print("no city")
                None

        except TypeError:
            # print("No location")
            None

    print(places)
    return places


def getTags(picture):
    app = ClarifaiApp("zHLcj-wack36gFK74waD7mrcfXX9eLJLd5D-26HY", "6bkZN7fpd9932i7dRd2uT278Qzejq4El7YMGijZx")
    # get the general model
    model = app.models.get("general-v1.3")
    tags = []


    # predict with the model
    model_thing = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
    jsonified = json.dumps(model_thing, sort_keys=True, indent=4, separators=(',', ': '))
    print(jsonified)
    json_data = json.loads(jsonified)
    for i in range(20):
        tag = json_data["outputs"]["data"]["concepts"][i]["name"]
        tags.append(tag)

    print(tags)
    return tags


getLocation()
getHashtags()
# getTags()
