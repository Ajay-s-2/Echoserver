import socket
HOST = '127.0.0.1'
PORT = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print(data.decode(), end="")
        except:
            break
import threading
threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        msg = input()
        if msg:
            client.sendall((msg + '\n').encode())
            if msg == "/quit":
                break
except:
    pass
client.close()
