# Multi-Threaded Echo Server

## Overview

This repository contains a multi-threaded implementation of a TCP/UDP-based echo server in Python. The server listens on a specified host and port, handling multiple client connections concurrently. Additionally, there is a client script to connect to the server and send a file.

## Files

- `echo-server.py`: Python script for the multi-threaded echo server.
- `echo-client.py`: Python script for the echo client.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/echo-server.git
   cd echo-server
   ```

2. **Run the Server:**
   ```bash
   python echo-server.py <protocol> <host> <port>
   ```
   - The server will start and bind to the specified host and port.

3. **Run the Client:**
   ```bash
   python echo-client.py <protocol> <host> <port> <file_path> <num_clients>
   ```
   - The client will connect to the server, send the content of the specified file, and receive the echoed response. The process is repeated for the specified number of clients.

4. **Modify and Experiment:**
   - Feel free to modify the server or client configurations to experiment with different scenarios.

## Requirements

- Python 3.x

## Contributing

If you would like to contribute to this project, please follow the steps mentioned in the [Contributing](#contributing) section below.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
