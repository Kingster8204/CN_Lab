import socket

def udp_server():
    # Server configuration
    host = "127.0.0.1"  # Localhost
    port = 12345        # Port to listen on

    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server is running on {host}:{port}")

    while True:
        # Receive data from the client
        data, client_address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message from {client_address}: {data.decode()}")

        # Echo the data back to the client
        response = f"Server received: {data.decode()}"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_server()
