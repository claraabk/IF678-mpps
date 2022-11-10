import socket
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0', 44325))
s.connect(('localhost',60200))

s.sendall(bytes('comece', 'utf-8'))
file = open('client_data/file.zip','wb')

while 1:

    data=s.recv(1024)

    if not data:
        break

    if data == b'terminei':
        print(data)
        break

    file.write(data)
 
s.close()