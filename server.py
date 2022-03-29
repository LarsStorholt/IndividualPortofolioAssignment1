import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8081))
server_socket.listen()

clients = []

#Message to all clients
def toAllClients(message):
    for client in clients:
        client.send(message)

def receive():
    while True:
        # Accept Connection
        client, address = server_socket.accept()

        client.send('xx'.encode('utf-8'))



        print(f"Connected with client on {str(address)}")

        #Recieve the name of the person joined the chat and print to server
        nickname = client.recv(1024).decode('utf-8')
        print(f'{nickname} joined')

        # adding client to clients
        clients.append(client)
        #Send to all client who joined
        toAllClients((f'{nickname} joined chat').encode('utf-8'))

        #toAllClients("heisann".encode('utf-8'))

        #message = client.recv(1024)
        #print(message.decode())
        #toAll(message)

        thread = threading.Thread(target=fromClientToClients, args=(client,))
        thread.start()


def fromClientToClients(client):
    while True:
        message = client.recv(1024)
        print(message.decode('utf-8'))
        toAllClients(message)



print('Server is ready...')
receive()