import socket
import threading

HOST = "127.0.0.1"
PORT = 65432

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    print(f"Connection with {addr} closed.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        client_handler = threading.Thread(target=handle_client, args=(conn, addr))
        client_handler.start()
