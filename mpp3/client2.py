from email import message
import socket
import threading
from datetime import datetime

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
nicknames = []
messagesNumber = 1
sentMessages = 0

def receive():
    while True:
            message = client.recv(1024).decode('ascii')

            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'new connection':
                client.close()
                break
            else:
                nicknames.append(message)
                """ print(message)
                print(nicknames[0]) """

def scndRcv():
    global messagesNumber
    global sentMessages
    while True:
            message = client.recv(1024).decode('ascii')

            if message == 'received':
                print(f'{nicknames[0]} diz #{sentMessages} recebida')
            else:
                date = datetime.now().strftime("%d/%m/%Y %H:%M")
                print(f'{nicknames[1]} #{messagesNumber} (enviado {message[0:16]}h/recebido {date}h):{message[18:]}')
                client.send('received'.encode('ascii'))

                messagesNumber += 1

def write():
    global sentMessages
    while True:
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        message = f'{date}: {input()}'
        client.send(message.encode('ascii'))

        sentMessages += 1
        print(f'{nicknames[1]} #{sentMessages} enviado {message} ')

receive()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((('127.0.0.1', 30000)))

receive_thread = threading.Thread(target=scndRcv)
receive_thread.start()

write_thread =  threading.Thread(target=write)
write_thread.start()