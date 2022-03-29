import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8000))
server_socket.listen()

clients = []

#Message to all clients
def toAll(message):
    for client in clients:
        client.send(message)

def receive():
    while True:
        # Accept Connection
        client, address = server_socket.accept()
        clients.append(client)
        print("Connected with {}".format(str(address)))

        #Recieve the name of the person joined the chat and print to server
        nickname = client.recv(1024).decode('utf-8')
        print(f'{nickname} joined')

        #Send to all client who joined
        toAll((f'{nickname} joined chat').encode('utf-8'))

        message = client.recv(1024)
        print(message.decode())
        #toAll(message)

        #thread = threading.Thread(target=handle, args=(client,))
        #thread.start()


#def handle(client):
 #   while True:
  #      message = client.recv(1024)
   #     toAll(message)



print('Server is ready...')
receive()