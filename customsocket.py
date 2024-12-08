import socket

class CustomSocket():

    def __init__(self, ip_address, port):
        self.max_packet_size = 516
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_address, port))
        print(f"Connected to {ip_address}:{port}")

    def send_data(self, data):
        client_socket.send(data.encode('utf-8'))

    def recieve_data(self):
        data = client_socket.recv(1024).decode('utf-8')
