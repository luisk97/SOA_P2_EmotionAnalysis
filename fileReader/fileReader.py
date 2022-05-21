# pylint: disable=C0103
# pylint: disable=C0114
import json

from flask import Flask

import requests

import include.rutils as util

PATH = "./images/"

app = Flask(__name__)

@app.route('/readImages', methods=['POST'])
def read_images():
    """ Handler for timer request, gets the request and reads the folder """
    images = util.readImages(PATH)
    images = json.dumps(images)
    if len(images) > 0:
        requests.post("http://analysis-app-deploy:7000/imgAnalysis", json=images)
        print('data sent')
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
