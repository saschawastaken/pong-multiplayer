import socket

class CustomSocket():

    def __init__(self, ip_address, port):
        self.max_packet_size = 516

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_listening(self, port):
        self.socket.bind(('', port))
        self.socket.listen(1)
        
        print(f"Server is listening on port {port}...")

    def listen(self):
        # Needs to be executed in the while loop.
    
        # Accept a client connection
        client_socket, client_address = self.socket.accept()
        print(f"Connection established with {client_address}")
        
        # Receive and echo data
        data = client_socket.recv(1024).decode('utf-8')
        
        if not data: return

        print(f"Received from client: {data}")

    def connect(self, ip_address, port):
        self.socket.connect((ip_address, port))
        print(f"Connected to {ip_address}:{port}")

    def send_data(self, data):
        self.socket.send(data.encode('utf-8'))
