import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    data = {'bid': '100', 'timestamp': time.time()}
    print(f"Send:{data}")
    socket.send_string(json.dumps(data))
    time.sleep(1)
