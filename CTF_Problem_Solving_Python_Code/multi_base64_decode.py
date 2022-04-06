import base64

with open('b64.txt') as f:
    msg=f.read()

for _ in range(50):
    msg=base64.b64decode(msg)

print(f"The flag is {msg.decode('utf8')}")
