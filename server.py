import socket

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable TCP Keep-Alive
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        print("Received:", data.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()
server_socket.close()
