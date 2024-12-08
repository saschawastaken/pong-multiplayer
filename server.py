import socket

PORT = 8000

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to a local address and port
    server_socket.bind(('', PORT))
    server_socket.listen(1)
    
    print(f"Server is listening on port {PORT}...")
    
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive and echo data
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received from client: {data}")
        client_socket.send(f"Echo: {data}".encode('utf-8'))
        
        # Close the connection
        client_socket.close()
        print("Connection closed")
        quit(0)

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        quit(0)
