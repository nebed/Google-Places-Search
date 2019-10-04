import os,sys
import requests
import json
import sqlite3
from collections import namedtuple
from re import sub
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS,cross_origin



app = Flask(__name__,
            static_folder = "./dist",
            template_folder = "./dist")

CORS(app)

GOOGLE_API = os.getenv('GOOGLE_API', '')
API_ENDPOINT = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'


@app.route('/find/', methods=['GET'])
@cross_origin()
def search_radius():
    location = request.args.get('location')
    radius = request.args.get('radius')
    keyword = request.args.get('keyword')
    place_type = request.args.get('type')
    PARAMS = {'location':location, 'radius':radius, 'keyword':keyword,'type':place_type,'key':GOOGLE_API}
    try:
        data = requests.get(url=API_ENDPOINT, params=PARAMS).json()
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    #print(soup)
    return data, 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home_page(path):
    return render_template('index.html'),200


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
