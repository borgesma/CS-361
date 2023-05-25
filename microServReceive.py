# Name: Marcello Borges
# Class: CS 361
# Filename: microServReceive.py
# Description: Implementation of microservice receive

# server side

import requests
import zmq
from bs4 import BeautifulSoup


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
socket.RCVTIMEO = 2000

while True:
    images_url_list = []
    try:
        #  Wait for next request from client
        message = socket.recv_string()
        split_message = message.split(",")
        search_query = split_message[0].replace(" ", "+")
        url = f"https://www.google.com/search?q={search_query}&tbm=isch"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img")
        for i in range(1, int(split_message[1]) + 1):
            images_url = images[i]["src"]
            images_url_list.append(images_url)

        #  Send reply back to client
        socket.send_json(images_url_list)

    except zmq.error.Again:
        break

socket.close()
context.term()
