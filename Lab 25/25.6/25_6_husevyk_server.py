import socket
import os

HOST = '127.0.0.1'
PORT = 65433

SAVE_DIR = "received_files"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Підключено: {addr}")
        filename = conn.recv(1024).decode()
        filepath = os.path.join(SAVE_DIR, filename)
        with open(filepath, "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"Файл збережено: {filepath}")