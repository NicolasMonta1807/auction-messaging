from flask import Flask, request

app = Flask(__name__)

@app.route('/track-bid', methods=['POST'])
def track_bid():
  bid_data = request.json
  
  print(f"Tracked bid: {bid_data}")
  return "Bid Tracked", 200

if __name__ == '__main__':
  app.run(port=5001)