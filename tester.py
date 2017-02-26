# TODO: Example Clarifai
# from clarifai.rest import ClarifaiApp
# import json
#
# app = ClarifaiApp("zHLcj-wack36gFK74waD7mrcfXX9eLJLd5D-26HY", "6bkZN7fpd9932i7dRd2uT278Qzejq4El7YMGijZx")
#
# # get the general model
# model = app.models.get("general-v1.3")
#
# # predict with the model
# model_thing = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
#
# print(json.dumps(model_thing, sort_keys=True, indent=4, separators=(',', ': ')))

# TODO: Example Airbnb
# import requests
# import json
#
# payloadBNB = {'client_id': '3092nxybyb0otqw18e8nh5nty', 'user_lat': '', 'user_lng': ''}
# r = requests.get('https://api.airbnb.com/v2/search_results', params=payloadBNB)
#
# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))

# TODO: Example Instagram
# import requests
# import json
#
# payload = {'access_token': '42404802.114b636.262414e1e9324e88a8d1de70562b3039'}
# r = requests.get('https://api.instagram.com/v1/users/self/media/liked', params=payload)
#
# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))
