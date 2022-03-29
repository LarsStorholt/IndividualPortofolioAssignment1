import socket
import threading

from bots import meldingFraBot

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

nickname = input("Choose a nickname: ")

def funksjon():
    while True:
        client_socket.send(nickname.encode())
        message = client_socket.recv(1024).decode('utf-8')
        print(message)
        input('')
        print(message)
        #print(f'{nickname}: {input("")}')


#def motattfraBots():
 #   print(meldingFraBot())

def writeInChat():
    message = f'{nickname}: {input("")}'
    #print(message)
    client_socket.send(message.encode('utf-8'))

#funksjon()
#writeInChat()

recieve_thread = threading.Thread(target=funksjon)
recieve_thread.start()

write_thread = threading.Thread(target=writeInChat())
write_thread.start()