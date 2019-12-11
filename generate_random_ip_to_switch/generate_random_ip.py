# generate randwom ip
import random
import socket
import struct
for i in range(512):
    ip_random = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    if ip_random == "0.0.0.0" or ip_random == "255.255.255.255":
        pass
        i = i-1
    else:
        print(ip_random)
