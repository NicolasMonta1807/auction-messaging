import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://producer:5555")  # Connect to the producer's address

while True:
    message = socket.recv_string()
    if "tracking" in message:
        print(f"Received message: {message}")
