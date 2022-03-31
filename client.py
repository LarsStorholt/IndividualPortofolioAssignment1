import socket
import threading
from list_of_words import *
from bots import *
import argparse

# Arguments to join right address and pot
argument = argparse.ArgumentParser()
argument.add_argument('ip', type=str)
argument.add_argument('port', type=int)
bothArg = argument.parse_args()

ip = bothArg.ip
port = bothArg.port

# Setting up socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

nickname = input("Choose a nickname: ")
nicknames = []
botnames = ['ingrid', 'ola', 'ellen', 'steffen']

def takeIn():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "xx":
                client_socket.send(nickname.encode())
            else:
                if nickname not in botnames:
                    print(message)

        except:
            print("error")
            client_socket.close()
            break


def inputChat():
    while True:
        if nickname not in botnames:
            message = f'{nickname}: {input("")}'

            client_socket.send(message.encode('utf-8'))

def fromBot():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        message_split = message.split()

        #'Find' answers from bots if the message is form a non-bot client
        if message_split[0].endswith(':') & (message_split[0][:-1] not in botnames):
            word = ''
            #Checking for a 'hello'-word
            for i in message_split:
                for j in hello_list:
                    if i == j:
                        word = i
                        break
                    else:
                        continue
                else:
                    continue
                break

            # Checking for a verb in verb-list
            for n in message_split:
                for m in verbs:
                    if n == m:
                        word = n
                        break
                    else:
                        continue
                else:
                    continue
                break

            #If the word wasnt found in lists
            if word != '':
                if nickname.lower() == 'ellen':
                    message_from_ellen = ellen(word)
                    client_socket.send(message_from_ellen.encode('utf-8'))

                elif nickname.lower() == 'ola':
                    message_from_ola = ola(word)
                    client_socket.send(message_from_ola.encode('utf-8'))

                elif nickname.lower() == 'steffen':
                    message_from_steffen = steffen(word)
                    client_socket.send(message_from_steffen.encode('utf-8'))

                elif nickname.lower() == 'ingrid':
                    message_from_ingrid = ingrid(word)
                    client_socket.send(message_from_ingrid.encode('utf-8'))

            else:
                message_from_bot = cantAsnwer()
                client_socket.send(message_from_bot.encode('utf-8'))


# Threads started
recieve_thread = threading.Thread(target=takeIn)
recieve_thread.start()

write_thread = threading.Thread(target=inputChat)
write_thread.start()

write_thread = threading.Thread(target=fromBot)
write_thread.start()