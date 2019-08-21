import scrapy
from flask import Flask
from flask import jsonify
from singlepage import QuotesSpider

app = Flask(__name__)

@app.route("/")
def hello():
  return 'hi'

# @app.route("/links/<variable>")
# def links(variable):
  # return variable
  # return singlepage.QuotesSpider.start_requests(variable)

@app.route("/links")
def links():
  thing = QuotesSpider.start_requests(true)
  return thing

if __name__ == '__main__':
    app.run(debug=True)

