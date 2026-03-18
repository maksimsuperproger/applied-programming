import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print("\nПовідомлення від іншого клієнта:", msg.decode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())