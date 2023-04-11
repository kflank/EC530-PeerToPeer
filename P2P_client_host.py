import socket
import threading

class P2P:
    # Set up server socket
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  

    def startServer(self):
            self.server.bind((self.HOST, self.PORT))
            self.server.listen()
            print(f"Server listening on {self.HOST}:{self.PORT}")


    def startClient(self):
        self.server.listen()
        self.client.connect((self.HOST, self.PORT))
        print(f"Connected to {self.HOST}:{self.PORT}")


    def handle_client(self, conn, addr):
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[{addr[0]}:{addr[1]}] {data}")
        conn.close()


    def receive_messages(self):
        while True:
            conn, addr = self.server.accept()
            print(f"Connected to {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def send_message(self):
        while True:
            message = input("")
            self.client.send(message.encode())



if __name__ == '__main__':
    HOST = input('Please insert IP address to host/connect server: ')
    PORT = int(input('Please insert Port Number: '))
    print(f'Your entered HOST IP address: {HOST}, your entered PORT number: {PORT}')
    p2p = P2P(HOST,PORT)

    option = input("Would you like to connect to a server (c) or set up a server (s)?")
    if option == 's':
        p2p.startServer()
        p2p.startClient()

    elif option == 'c':
        p2p.startClient()
        
    
    # Start the threads for receiving and sending messages
    receive_thread = threading.Thread(target=p2p.receive_messages)
    send_thread = threading.Thread(target=p2p.send_message)
    receive_thread.start()
    send_thread.start()
    

