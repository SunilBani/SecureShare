import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"Listening on port {PORT}...")

conn, addr = server.accept()
print(f"Connected to {addr}")

with open("received.enc", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("Encrypted file received!")
conn.close()
