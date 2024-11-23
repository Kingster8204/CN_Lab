import socket

def udp_client():
    # Server configuration
    server_host = "127.0.0.1"  # Server IP
    server_port = 12345        # Server port

    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Input message to send
        message = input("Enter message to send to server (or type 'exit' to quit): ")
        if message.lower() == "exit":
            print("Exiting client.")
            break

        # Send data to server
        client_socket.sendto(message.encode(), (server_host, server_port))

        # Receive response from server
        data, server_address = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Response from server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()
