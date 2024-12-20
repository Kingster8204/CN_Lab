import socket

def start_server():
    # Define server address and port
    host = '127.0.0.1'  # Localhost
    port = 65432        # Non-privileged port

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one connection at a time
    print(f"Server listening on {host}:{port}...")

    # Accept a client connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        # Receive data from the client
        data = conn.recv(1024)  # Buffer size
        if not data:
            break
        print(f"Received from client: {data.decode()}")

        # Send a response to the client
        conn.sendall(b"Hello, Dev")

    # Close the connection
    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_server()
