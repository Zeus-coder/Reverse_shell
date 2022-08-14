#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 54321))
print("Connected to the server")
s.close()
