import socket
import json # wär isch jason?
import threading


def receive_movements(conn):
    global CLIENT_KEYBOARD_EVENTS
    
    connected = True

    while connected:
        # Receive and echo data
        data = conn.recv(1024).decode('utf-8')
        
        if not data: return

        print(f"Received from client: {data}")

        CLIENT_KEYBOARD_EVENTS = json.loads(data)

class CustomSocket():

    def __init__(self):
        self.max_packet_size = 516

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.connection = None
        self.client_address = None

    # SERVER SHIT

    def start_listening(self, port):
        self.socket.bind(('', port))
        self.socket.listen(1)
        
        print(f"Server is listening on port {port}...")

        # Accept a client connection
        self.connection, self.client_address = self.socket.accept()

        thread = threading.Thread(target=receive_movements, args=(self.connection,))

        thread.start()

        print(f"Connection established with {self.client_address}")

    # CLIENT SHIT

    def connect(self, ip_address, port):
        self.socket.connect((ip_address, port))
        print(f"Connected to {ip_address}:{port}")

    def send_movements(self, keyboard_events):
        json_data = json.dumps(keyboard_events, indent = 4) .encode('utf-8')
        self.socket.sendall(json_data)
    
    def close(self):
        self.socket.close()
