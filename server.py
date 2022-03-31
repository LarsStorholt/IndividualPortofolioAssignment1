import socket
import threading
import argparse

# Port you want to join on
arg = argparse.ArgumentParser()
arg.add_argument('port', type=int)
allArg = arg.parse_args()
port = allArg.port

# Setting up socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", port))
server_socket.listen()

clients = []
bots = ['ellen', 'ola', 'steffen', 'ingrid']

# Broadcast message to all clients
def toAllClients(message):
    for client in clients:
        client.send(message)

def accept():
    while True:
        # Accept Connection
        client, address = server_socket.accept()

        client.send('xx'.encode('utf-8'))

        # Printed to server which address the server is connected to client
        print(f"Connected with client on {str(address)}")

        #Recieve the name of the person joined the chat and print to server
        nickname = client.recv(1024).decode('utf-8')
        if nickname in bots:
            print(f'Chatbot {nickname} joined')
        else:
            print(f'{nickname} joined')

        # adding client to clients-list
        clients.append(client)

        #Send to all client who joined
        if nickname in bots:
            toAllClients((f'Chatbot {nickname} joined chat, and are ready to mingle').encode('utf-8'))
        else:
            toAllClients((f'{nickname} joined chat').encode('utf-8'))


        thread = threading.Thread(target=fromClientToClients, args=(client,))
        thread.start()

#Sends the messages recieved from a client, out to all clients
def fromClientToClients(client):
    while True:
        message = client.recv(1024)
        print(message.decode('utf-8'))
        toAllClients(message)

print('Server is ready...')
accept()