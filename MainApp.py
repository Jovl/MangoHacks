"""
MainApp.py

Author: Jeremiah Lantzer

Travel reccomendations on a budget.

Insta Auth Token Jeremiah: 42404802.114b636.262414e1e9324e88a8d1de70562b3039
Insta Auth Token Kelly: 22220287.114b636.9b53377e1cb84493a59a7950b16795bd
"""

from flask import Flask, render_template
import backend

app = Flask(__name__)


@app.route('/login')
def login():
    return


if __name__ == "__main__":
    app.run()
