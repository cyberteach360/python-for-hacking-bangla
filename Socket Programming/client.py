#!/usr/bin/python

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1",54321))
print("The connetion is Established to Server")
while True:
    data = sock.recv(1024)
    print(data)
    if data == "q":
        break
    else:
        message_back = raw_input("Type message to send to Server:")
        sock.send(message_back)

sock.close()
