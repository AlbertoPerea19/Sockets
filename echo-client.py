import socket
import sys

HOST, PORT, FILE_PATH = sys.argv[1], int(sys.argv[2]), sys.argv[3]
num_clients=int(sys.argv[4])

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Open the file and read its content
        with open(FILE_PATH, 'rb') as file:
            file_content = file.read()

        s.sendall(file_content)
        data = s.recv(1024)
        print(f"Received {data!r}")

if __name__ == "__main__":
    # Simulate multiple clients
    for _ in range(num_clients):
        run_client()
