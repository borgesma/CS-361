# Name: Marcello Borges
# Class: CS 361
# Filename: microServSend.py
# Description: Implementation of microservice send

# client side

import zmq
import microServReceive

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

requests = ['Chimp monkeys', '2']

socket.send_string(requests[0] + "," + requests[1])
list_of_links = socket.recv_json()

print(list_of_links)
