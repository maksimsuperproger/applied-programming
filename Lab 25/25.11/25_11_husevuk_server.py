import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clients = []

def handle_client(client_socket, other_client):
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            if other_client:
                other_client.sendall(msg)
        except:
            break
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(2)
    while len(clients) < 2:
        client_socket, addr = server.accept()
        print(f"Підключено: {addr}")
        clients.append(client_socket)

    threading.Thread(target=handle_client, args=(clients[0], clients[1]), daemon=True).start()
    threading.Thread(target=handle_client, args=(clients[1], clients[0]), daemon=True).start()

    print("Два клієнти підключено. So it begins")
    threading.Event().wait()