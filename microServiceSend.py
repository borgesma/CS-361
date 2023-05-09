# Name: Marcello Borges
# Class: CS 361
# Filename: microServiceSend.py
# Description: Implementation of microservice send

import zmq
from subprocess import call

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7000")
call(["python", "microServiceReceive.py"])

image_search = input("What image would you like to search for? ")
number_of_images = input("How many images of " + image_search + " would you like to search for? ")
requests = [image_search, number_of_images]
responses = []

for request in requests:
    socket.send_string(request)
    message = socket.recv_string()
    responses.append(message)

print(responses)
