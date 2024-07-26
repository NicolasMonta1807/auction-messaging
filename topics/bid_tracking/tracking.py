import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    message = socket.recv_string()
    data = json.loads(message)
    print(f"Tracked: {data}")
