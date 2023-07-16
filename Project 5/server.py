import socket
import threading
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print("Encryption key:", key)
cipher_suite = Fernet(key)

def start_server():
    # Using local host
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 50000))

    server.listen()

    while True:
        # Accept a new client and get the client socket and address
        client_socket, client_address = server.accept()

        print("Accepted connection from ", client_address)

        # Handle client in a separate thread
        threading.Thread(target=client_handler, args=(client_socket,)).start()


def client_handler(client_socket):
    while True:
        # Get the message from the client
        message = client_socket.recv(1024)

        if not message:
            break

        # Decrypt the message
        decrypted_message = cipher_suite.decrypt(message)
        print("Received message: ", decrypted_message.decode())

        # Encrypt the message
        encrypted_message = cipher_suite.encrypt(decrypted_message)

        # Send the message to all clients
        for client in clients:
            client.send(encrypted_message)

    # Remove the client from the list and close the socket
    clients.remove(client_socket)
    client_socket.close()


clients = []

# Start the server
start_server()
