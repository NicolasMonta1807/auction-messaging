from flask import Flask, request

app = Flask(__name__)

@app.route('/analyse-bid', methods=['POST'])
def analyse_bid():
  bid_data = request.json
  
  print(f"Analysed bid: {bid_data}")
  return "Bid Analysed", 200

if __name__ == '__main__':
  app.run(port=5002)