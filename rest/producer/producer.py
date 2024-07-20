from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT = os.getenv("PORT")

service_urls = {
  "capture": os.getenv("CAPTURE_URL"),
  "tracking": os.getenv("TRACKING_URL"),
  "analytics": os.getenv("ANALYTICS_URL")
}

@app.route('/produce-bid', methods=['POST'])
def produce_bid():
  bid_data = request.json
  
  # TODO: Modify bid data for each service
  capture_response = requests.post(service_urls["capture"], json=bid_data)
  
  tracking_response = requests.post(service_urls["tracking"], json=bid_data)
  
  analytics_response = requests.post(service_urls["analytics"], json=bid_data)
  
  return jsonify({
    "capture": capture_response.text,
    "tracking": tracking_response.text,
    "analytics": analytics_response.text
  }), 200
  
  
if __name__ == '__main__':
  app.run( port=PORT)
  