import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

with open("encrypted_files/test.enc", "rb") as f:
    client.sendall(f.read())

print("Encrypted file sent!")
client.close()
