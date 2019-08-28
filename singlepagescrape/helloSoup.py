from flask import Flask
from flask import jsonify
from scraping import scrape
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/<var>', methods=['GET'])
def index(var):
    return jsonify(Links=scrape(var))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)



