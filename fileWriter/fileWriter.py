# pylint: disable=W0311
# pylint: disable=C0103
# pylint: disable=C0114
import json

from flask import Flask, request
from flask_restful import Api # pylint: disable=E0401

import include.wutils as util

PATH = "./results/analysisLog.txt"

app = Flask(__name__)
api = Api(app)

@app.route("/results", methods=['POST'])
def listener():
        """ Handler for post requests, gets a list of results with the analysis """
        request_simple = request.get_json()
        parsed_res = json.loads(request_simple)
        util.writeResult(PATH,parsed_res)
        return "ok"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
