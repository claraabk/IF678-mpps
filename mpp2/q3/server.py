import socket, time

localPort = 60200
bufferSize = 1024

msgFromServer = bytes('Hello UDP Client', 'utf-8')

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind(('localhost', localPort))

while True:

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address =  bytesAddressPair[1]

    if message == b'comece':
        print(message.decode())

        arq=open('data/file.zip','rb')
        for i in arq:
            UDPServerSocket.sendto(i, address)
    
        arq.close()

        time.sleep(1)
        UDPServerSocket.sendto((bytes('terminei', 'utf-8')), address)
        break

UDPServerSocket.close()