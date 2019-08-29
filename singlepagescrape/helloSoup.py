from flask import Flask
from flask import jsonify
from flask import request
from scraping import scrape
from scrapingClick import scrapeClick
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# cors = CORS(app, resources={r"*": {"origins": "*"}})
cors = CORS(app)

@app.route('/links', methods=['POST'])

# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def index():
    data = request.json
    print(data)
    return jsonify(Links=scrape(data))
    # return jsonify(data)
    # print(data['url'])
    # return data

@app.route('/click/<variable>', methods=['GET'])
def index2(variable):
    return jsonify(Links=scrapeClick(variable))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



