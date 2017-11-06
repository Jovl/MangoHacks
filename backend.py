"""
backend.py

Author: Jeremiah Lantzer
# hello world
Travel reccomendations on a budget.

Insta Auth Token Jeremiah:  XXXXXXX
Insta Auth Token Kelly:  XXXXXXX
"""

import requests
import json
import re
from geopy.geocoders import Nominatim

payload = {'access_token': ' XXXXXXX'}


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
    geolocator = Nominatim()
    r = requests.get('https://api.instagram.com/v1/users/self/media/liked', params=payload)
    jsonifier = json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    print(jsonifier)
    locations = {}
    locations['Location'] = []
    y = 0
    json_data = json.loads(jsonifier)
    locations["Location"] = []

    for x in range(20):
        try:
            latitude = json_data["data"][x]["location"]["latitude"]
            longitude = json_data["data"][x]["location"]["longitude"]
            # print(latitude)
            # print(longitude)
            lat_long = "%f, %f" % (latitude, longitude)
            location = geolocator.reverse(lat_long)
            raw = location.raw
            print(raw)
            rawJson = json.dumps(raw, sort_keys=True, indent=4, separators=(',', ': '))
            raw_json = json.loads(rawJson)


            try:
                city = raw_json["address"]["city"]
                state = raw_json["address"]["state"]
                location_str = city + ", " + state
                image_url = json_data["data"][x]["images"]["standard_resolution"]["url"]
                airbnb = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&user_lat=%s&user_lng=%s' % (
                latitude, longitude)
                locations["Location"] += [({"name": location_str, "image_url": image_url, "airbnb_url": airbnb})]

            except KeyError:
                city = "No city"
                state = raw_json["address"]["state"]
                location_str = city + ", " + state
                image_url = json_data["data"][x]["images"]["standard_resolution"]["url"]
                airbnb = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&user_lat=%s&user_lng=%s' % (
                latitude, longitude)

                locations["Location"] += [({"name": location_str, "image_url": image_url, "airbnb_url": airbnb})]

        except TypeError:
            # print("No location")
            None

    print(locations)
    return locations


getLocations()
# getHashtags()
# getTags()
