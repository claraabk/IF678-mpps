from opcode import opname
import socket

serverAddressPort = ('localhost', 60200)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytes('comece', 'utf-8'), serverAddressPort)
file = open('client_data/file.zip','wb')

while 1:
    msgFromServer =  UDPClientSocket.recvfrom(bufferSize)
    data = msgFromServer[0]

    if data == b'terminei':
        print(data.decode())
        break

    file.write(data)

UDPClientSocket.close()