import socket
import sys

PROTOCOL, HOST, PORT, FILE_PATH = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
NUM_CLIENTS = int(sys.argv[5])
BUFFER_SIZE = 1024  # Tamaño del búfer de lectura/envío

def socket_protocol(protocol):
    if protocol == 'TCP':
        return socket.SOCK_STREAM
    elif protocol == 'UDP':
        return socket.SOCK_DGRAM
    else:
        raise ValueError("Please choose TCP or UDP for the protocol")

def run_client():
    with socket.socket(socket.AF_INET, socket_protocol(PROTOCOL)) as s:
        s.connect((HOST, PORT))

        with open(FILE_PATH, 'rb') as file:
            while True:
                file_data = file.read(BUFFER_SIZE)
                if not file_data:
                    break  # Fin del archivo

                s.sendto(file_data, (HOST, PORT))

        print("File sent successfully")

if __name__ == "__main__":
    for _ in range(NUM_CLIENTS):
        run_client()
