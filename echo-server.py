import socket
import sys
import threading

PROTOCOL, HOST, PORT = sys.argv[1], sys.argv[2], int(sys.argv[3])

def socket_protocol(protocol):
    if protocol == 'TCP':
        return socket.SOCK_STREAM
    elif protocol == 'UDP':
        return socket.SOCK_DGRAM
    else:
        raise ValueError("Please choose TCP or UDP for the protocol")

def handle_client(data, addr):
    print(f"Received data from {addr}: {data}")
    # Aquí puedes realizar cualquier procesamiento adicional que necesites

try:
    with socket.socket(socket.AF_INET, socket_protocol(PROTOCOL)) as s:
        s.bind((HOST, PORT))
        if PROTOCOL == 'TCP':
            s.listen()
            print(f"Server listening on {HOST}:{PORT}")

        while True:
            if PROTOCOL == 'TCP':
                conn, addr = s.accept()
                client_handler = threading.Thread(target=handle_client, args=(conn.recv(1024), addr))
                client_handler.start()
            else:
                data, addr = s.recvfrom(1024)
                client_handler = threading.Thread(target=handle_client, args=(data, addr))
                client_handler.start()
except socket.error as e:
    print(f"Socket error: {e}")
