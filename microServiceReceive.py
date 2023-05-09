# Name: Marcello Borges
# Class: CS 361
# Filename: microServiceReceive.py
# Description: Implementation of microservice receive

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7000")

while True:
    message = socket.recv_string()
    socket.send_string(f"{message}")
