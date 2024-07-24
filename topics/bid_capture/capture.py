import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://producer:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    message = socket.recv_string()
    data = json.loads(message)
    print(f"Captured: {data}")