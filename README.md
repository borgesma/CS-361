# CS361-Microservice - Marcello Borges

Microservice for partner's project in CS361.

# Communication Contract
How do you request data from the microservice?

You can request data from the microservice by first running the microServiceSend.py file and then running the python file microServiceSend.py; the user is then prompted to input the image it would like to search and how many of those images they'd like to see. The microServiceSend.py file will then send data to the microServiceReceive.py file.

How do you receive data from the microservice?

The data is then received by the same way it is requested. Once you input data requested, it will send the data to the microServiceReceive.py file and return a response to the microServiceSend.py file as a list of values.


# UML Sequence Diagram

![image](https://user-images.githubusercontent.com/102485058/236998095-2d9b31a8-66f6-4436-ac6e-2f0278d10d7c.png)
