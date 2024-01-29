import socket

HOST = "127.0.0.1"
PORT = 65432
FILE_PATH = "helloWorld.txt"

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
    num_clients = 3
    for _ in range(num_clients):
        run_client()
