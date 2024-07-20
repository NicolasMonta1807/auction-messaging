from flask import Flask, request

app = Flask(__name__)

@app.route('/tracking-bid', methods=['POST'])
def capture_bid():
  bid_data = request.json
  
  print(f"Captured bid: {bid_data}")
  return "Bid Captured", 200

if __name__ == '__main__':
  app.run(port=5001)