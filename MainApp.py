"""
MainApp.py

Author: Jeremiah Lantzer

Travel reccomendations on a budget.

Insta Auth Token Jeremiah: XXXXXXX
Insta Auth Token Kelly: XXXXXXX
"""

from flask import Flask, jsonify
import backend

app = Flask(__name__)
backend = backend

# @app.route('/hashtags')
# def hashtags():
#     return backend.getHashtags()


@app.route('/locations')
def locations():
    json = jsonify(backend.getLocations())
    print(json)
    return json


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)       # set host= to
