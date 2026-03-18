import socket

HOST = '127.0.0.1'
PORT = 65434

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    v = input("Введіть ваш, можливо, неправильний вираз: ")
    s.sendall(v.encode())

    data = s.recv(1024)
    print("Server response:", data.decode())