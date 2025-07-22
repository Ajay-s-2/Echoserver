import socket
import threading
import os
from datetime import datetime

HOST = '0.0.0.0'
PORT = 1024

clients = {}
usernames = {}

# Load user credentials
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if ':' in line:
                    u, p = line.strip().split(':')
                    users[u] = p
    return users

user_db = load_users()

# Broadcast message to all connected clients
def broadcast(sender, msg):
    for user, conn in clients.items():
        if user != sender:
            try:
                conn.sendall(f"[{sender}] {msg}\n".encode())
            except:
                continue

# Handle individual client
def handle_client(conn, addr):
    conn.sendall("Welcome to Echo Server!\nLogin with username:\n".encode())
    username = conn.recv(1024).decode().strip()

    conn.sendall("Enter password:\n".encode())
    password = conn.recv(1024).decode().strip()

    if username in user_db and user_db[username] == password:
        conn.sendall(f"Login successful. Hello, {username}!\nType /help for commands.\n".encode())
        clients[username] = conn
        usernames[conn] = username
        log_message(f"{username} connected from {addr[0]}:{addr[1]}")

        # Start communication
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                msg = data.decode().strip()

                # Save message history
                save_history(username, msg)

                if msg.startswith("/"):
                    if msg == "/quit":
                        conn.sendall("Disconnected from server.\n".encode())
                        break
                    elif msg == "/help":
                        conn.sendall("/help - show commands\n/users - list users\n/quit - disconnect\n/history - get your message history\n".encode())
                    elif msg == "/users":
                        conn.sendall(f"Active users: {', '.join(clients.keys())}\n".encode())
                    elif msg == "/history":
                        history = get_history(username)
                        conn.sendall(history.encode())
                    else:
                        conn.sendall("Unknown command. Type /help\n".encode())
                else:
                    # Echo back to sender
                    conn.sendall(f"You said: {msg}\n".encode())
                    broadcast(username, msg)
                    log_message(f"[{username}] {msg}")

            except:
                break
    else:
        conn.sendall("Invalid credentials. Connection closed.\n".encode())

    # Cleanup
    if username in clients:
        del clients[username]
    conn.close()
    log_message(f"{username} disconnected.")

# Save all logs
def log_message(msg):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/chatlog.txt", "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

# Save per-user history
def save_history(username, msg):
    os.makedirs("history", exist_ok=True)
    with open(f"history/{username}.txt", "a") as f:
        f.write(msg + "\n")

def get_history(username):
    path = f"history/{username}.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return "No history found.\n"

# Start Server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[+] Server started on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
