import socket
import json

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable TCP Keep-Alive
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

client_socket.connect((HOST, PORT))

data_to_send = {"key": "value"}

try:
    while True:
        message = json.dumps(data_to_send).encode('utf-8')
        client_socket.sendall(message)
        print("Data sent:", data_to_send)
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
