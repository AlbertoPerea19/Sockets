# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
FILE_PATH="helloWorld.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open(FILE_PATH, 'rb') as file:
        file_content = file.read()

    s.sendall(file_content)
    data = s.recv(1024)

print(f"Received {data!r}")
