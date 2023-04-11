import subprocess
import time

import pytest
 
# drafted with chat gpt

@pytest.fixture
def listening_server():
    # Start the server in listening mode as a subprocess
    server = subprocess.Popen(["python", "p2p_communication.py", "--listen"], stdout=subprocess.PIPE)

    # Wait for the server to start up
    time.sleep(1)

    # Return the subprocess object
    yield server

    # Terminate the subprocess after the test is finished
    server.terminate()


def test_connect_to_server(listening_server):
    # Test that we can connect to the server and receive a welcome message
    client = subprocess.Popen(["python", "p2p_communication.py", "--connect", "localhost"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = client.stdout.readline().decode().strip()
    assert output == "Connected to server"

    # Send a message to the server
    client.stdin.write(b"Hello, server!\n")
    client.stdin.flush()

    # Receive the response from the server
    output = client.stdout.readline().decode().strip()
    assert output == "Server: Hello, client!"

    # Clean up
    client.terminate()


def test_send_receive_message(listening_server):
    # Test sending and receiving a message between two clients
    client1 = subprocess.Popen(["python", "p2p_communication.py", "--connect", "localhost"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = client1.stdout.readline().decode().strip()
    assert output == "Connected to server"

    client2 = subprocess.Popen(["python", "p2p_communication.py", "--connect", "localhost"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = client2.stdout.readline().decode().strip()
    assert output == "Connected to server"

    # Send a message from client 1 to client 2
    client1.stdin.write(b"Hello, client 2!\n")
    client1.stdin.flush()

    # Receive the message on client 2
    output = client2.stdout.readline().decode().strip()
    assert output == "Client 1: Hello, client 2!"

    # Send a response from client 2 to client 1
    client2.stdin.write(b"Hello, client 1!\n")
    client2.stdin.flush()

    # Receive the response on client 1
    output = client1.stdout.readline().decode().strip()
    assert output == "Client 2: Hello, client 1!"

    # Clean up
    client1.terminate()
    client2.terminate()
