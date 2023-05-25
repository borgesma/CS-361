# CS361-Microservice - Marcello Borges

Microservice for partner's project in CS361.

# Communication Contract
**How do you request data from the microservice?**

You can request data from the microservice by first running the microServSend.py file. What should be sent over the socket is a list where index 0 is a string of a word search and index 1 is a string of the number of images that program wants URLs for. The microServiceSend.py file will then send that list with length 2 to the microServReceive.py file, process it, create image URLs for those search phrase string. This should be sent over with the port number 5555.

**How do you receive data from the microservice?**

The data received from the microservice is a json of a list of the image URLs for the search phrase. The list will be of the length that the client side program input as index 1 in the initial request data list.


# UML Sequence Diagram

![image](https://github.com/borgesma/CS-361/assets/102485058/d2f57d4d-7476-49a6-8597-8ee5f81a3ceb)


