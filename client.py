import socket
import threading

from bots import meldingFraBot

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8081))

nickname = input("Choose a nickname: ")

def recieve():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "xx":
                client_socket.send(nickname.encode())
            else:
                print(message)
                #input('')

                #print(f'{nickname}: {input("")}')
        except:
            print("error")
            client_socket.close()
            break


#def motattfraBots():
 #   print(meldingFraBot())

def writeInChat():
    while True:
        message = f'{nickname}: {input("")}'
        #print(message)
        client_socket.send(message.encode('utf-8'))

#funksjon()
#writeInChat()

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=writeInChat)
write_thread.start()