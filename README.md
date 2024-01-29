# Echo Server-Client

## Overview

This repository contains a simple implementation of a TCP-based echo server and client in Python. The echo server listens on a specified port, and the client connects to it, sends a message, and receives the echoed response.

## Files

- `echo-server.py`: Python script for the echo server.
- `echo-client.py`: Python script for the echo client.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/echo-server-client.git
   cd echo-server-client
   ```

2. **Run the Server:**
   ```bash
   python echo-server.py
   ```
   - The server will start and bind to the localhost on port 65432.

3. **Run the Client:**
   ```bash
   python echo-client.py
   ```
   - The client will connect to the server, send the message "Hello, world," and receive the echoed response.

4. **Modify and Experiment:**
   - Feel free to modify the messages, server port, or client configurations to experiment with different scenarios.

## Requirements

- Python 3.x

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork locally.
   ```bash
   git clone https://github.com/your-username/echo-server-client.git
   cd echo-server-client
   ```
3. Create a new branch for your changes.
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make your changes and commit them.
   ```bash
   git add .
   git commit -m "Add your feature or fix"
   ```
5. Push your changes to your fork.
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
