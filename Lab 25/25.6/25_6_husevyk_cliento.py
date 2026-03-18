import socket
import os

HOST = '127.0.0.1'
PORT = 65433

filepath = input("path: ")

if not os.path.exists(filepath):
    print("не існує файлу")
    exit()

filename = os.path.basename(filepath)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(filename.encode())
    response = s.recv(1024)
    with open(filepath, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)

    print("Файл відправлено!")