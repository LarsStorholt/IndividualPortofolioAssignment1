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
                if not message.startswith('lars'):
                    print(message)
                    fromBot(message)

                #elif nickname == 'ingrid':
                   # client_socket.send('hei'.encode('utf-8'))

                #split_message = re.split(r'\s +|[,;?!.-]\s*', message.lower())
                #splitMessage = message.lower.split()
                #if nickname.lower == 'ingrid':
                #    word = ''
                #    for i in splitMessage:
                #        for j in list_of_words.verbs:
                #            if i == j: word = i
                #    if not word:
                #        client_socket.send('Didnt understand'.encode('utf-8'))
                #    else:
                #        botResponse = bots.Ingrid(word)
                #        client_socket.send(botResponse.encode('utf-8'))
                #input('')
                #if nickname not in ['ellen','ola', 'steffen', 'ingrid']:

                #print(message)

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

def fromBot(message):
    #message = client_socket.recv(1024).decode('utf-8')
    message_split = message.split()
    #calls messages from bots if the message is a chat-message from a host
    if message_split[0].endswith(':') & (message_split[0][:-1] not in botnames):
        message_from_bot = bots.meldingFraBot()
        client_socket.send(message_from_bot.encode('utf-8'))



            #else: print('Ikke chat-melding')
#funksjon()
#writeInChat()

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=writeInChat)
write_thread.start()

#write_thread = threading.Thread(target=fromBot)
#write_thread.start()