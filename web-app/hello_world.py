import os
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("Hello world!")
print(os.environ.get('PORT'))
print(os.listdir())
print(os.listdir(os.path.join(os.path.abspath("."), 'app')))
print(local_ip)

current_directory = os.path.dirname(os.path.abspath(__file__))
print(os.listdir())
print(os.path.join(current_directory, "x"))
