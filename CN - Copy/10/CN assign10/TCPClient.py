import socket

def start_client():
    # Define server address and port
    host = '127.0.0.1'  # Server's IP address
    port = 65432        # Server's port

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")

    try:
        # Send a message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        print(f"Sent to server: {message}")

        # Receive a response from the server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
