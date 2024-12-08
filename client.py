import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect(('localhost', 12345))
    print("Connected to server")
    
    # Send a message
    message = "Hello, Server!"
    client_socket.send(message.encode('utf-8'))
    print(f"Sent to server: {message}")
    
    # Receive the echoed message
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {data}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
