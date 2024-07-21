import time
import random
import zmq

# Get user input
interval = 2
num_requests = 100

# Initialize ZeroMQ context
context = zmq.Context()

# Create a PUSH socket
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5555")  # Bind to a port

services = ["capture", "tracking", "analytics"]
count = 0

while num_requests == -1 or count < num_requests:
    service = random.choice(services)
    message = f"{service}"
    print(f"Enviando mensaje a {message}")
    socket.send_string(message)
    time.sleep(interval)
    count += 1

print("Termina.")
