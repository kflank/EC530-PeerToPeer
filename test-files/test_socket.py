import socket
import threading

# set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# get user input for IP and port
ip = input("Enter the IP address of the other user: ")
port = int(input("Enter the port number of the other user: "))

# connect to other user
s.connect((ip, port))

# send and receive messages
def send_msg():
    while True:
        msg = input("You: ")
        s.send(msg.encode())

def recv_msg():
    while True:
        msg = s.recv(1024).decode()
        print("Other user:", msg)

# start threads for sending and receiving messages
send_thread = threading.Thread(target=send_msg)
recv_thread = threading.Thread(target=recv_msg)

send_thread.start()
recv_thread.start()
