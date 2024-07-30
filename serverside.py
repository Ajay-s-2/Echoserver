import socket

HOST = ''  # Bind to all available interfaces
PORT = 1024

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"Server listening on port {PORT}")

# Accept a connection
conn, addr = s.accept()
print(f"{addr[0]} connected with back port {addr[1]}")

# Start communication loop
buffer = ""
while True:
    data = conn.recv(1024)
    if not data:
        break

    buffer += data.decode()
    if '\n' in buffer:
        # Split the buffer into complete messages and the remaining partial message
        messages = buffer.split('\n')
        for message in messages[:-1]:
            if message.lower().strip() == "quit":
                conn.sendall("Goodbye!\n".encode())
                break
            else:
                conn.sendall((message + '\n').encode())
        buffer = messages[-1]

conn.close()
s.close()
