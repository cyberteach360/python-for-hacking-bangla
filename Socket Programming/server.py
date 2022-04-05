#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("127.0.0.1",54321))
s.listen(5)
print("Listening for Incoming Connections")
target,ip =s.accept()
print("Target is Connected")
while True:
    data = raw_input("Enter your message:")
    target.send(data)
    if data == "q":
        break
    else:
        answer = target.recv(1024)
        print(answer)
s.close() 
