import socket
import ast

HOST = '127.0.0.1'
PORT = 65434

def is_valid_expression(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if not isinstance(node, (
                ast.Expression,
                ast.BinOp,
                ast.UnaryOp,
                ast.Constant,
                ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                ast.USub,
                ast.Load,
                ast.Constant,
                ast.Mod,
                ast.FloorDiv
            )):
                return False
        return True
    except:
        return False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Сервер запущенo")

    conn, addr = s.accept()
    with conn:
        print(f"Підключено: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            expr = data.decode()

            if is_valid_expression(expr):
                response = "good"
            else:
                response = "bad"

            conn.sendall(response.encode())