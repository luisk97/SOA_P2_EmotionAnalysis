# pylint: disable=C0103
# pylint: disable=C0114
import json

from flask import Flask, request

import requests

import include.visionConnect as visWrap

app = Flask(__name__)

@app.route('/imgAnalysis', methods=['POST'])
def img_analysis():
    """Listener for post method, containing an array of images to process"""
    jsondata = request.get_json()
    data = json.loads(jsondata)
    if len(data) > 0:
        response = visWrap.visionResponse(data)
        response = json.dumps({"results":response})
        requests.post("http://file-writer-app-deploy:8000/results", json=response)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True, threaded=False)
