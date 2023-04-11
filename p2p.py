import socket
import threading
import UIkit.testUI

# Set up server socket
HOST = '172.20.10.8'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind((HOST, PORT))
server.listen()

# Set up client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"[{addr[0]}:{addr[1]}] {data}")
    conn.close()

def receive_messages():
    while True:
        conn, addr = server.accept()
        print(f"Connected to {addr[0]}:{addr[1]}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def send_message():
    while True:
        message = input("")
        client.send(message.encode())

# Start the threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_message)

receive_thread.start()
send_thread.start()
