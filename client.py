import socket
import threading
import re
import list_of_words
import bots



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8081))

nickname = input("Choose a nickname: ")
nicknames = []
botnames = ['ingrid', 'ola', 'ellen', 'steffen']

def recieve():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "xx":
                client_socket.send(nickname.encode())
            else:
                if nickname not in botnames:
                    print(message)
                    #fromBot(message)
        except:
            print("error")
            client_socket.close()
            break


def writeInChat():
    while True:
        message = f'{nickname}: {input("")}'
        #print(message)
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
                for j in list_of_words.hello_list:
                    if i == j:
                        word = i
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break

            # Checking for a verb in verb-list
            for n in message_split:
                for m in list_of_words.verbs:
                    if n == m:
                        word = n
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break

            if nickname.lower() == 'ellen':
                message_from_ellen = bots.ellen(word)
                print(message_from_ellen)
                client_socket.send(message_from_ellen.encode('utf-8'))

            elif nickname.lower() == 'ola':
                message_from_ola = bots.ola(word)
                print(message_from_ola)
                client_socket.send(message_from_ola.encode('utf-8'))

            elif nickname.lower() == 'steffen':
                message_from_steffen = bots.steffen(word)
                print(message_from_steffen)
                client_socket.send(message_from_steffen.encode('utf-8'))

            elif nickname.lower() == 'ingrid':
                message_from_ingrid = bots.ingrid(word)
                print(message_from_ingrid)
                client_socket.send(message_from_ingrid.encode('utf-8'))

            else:
                message_from_bot = 'Bots: I`m sorry, but we do not have a good answer to that'
                client_socket.send(message_from_bot.encode('utf-8'))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=writeInChat)
write_thread.start()

write_thread = threading.Thread(target=fromBot)
write_thread.start()