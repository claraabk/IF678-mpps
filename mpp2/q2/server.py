import socket, time
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 60200))
s.listen(1)
 
conn,addr= s.accept()

while 1:
    data = conn.recv(1024).decode()

    if data == 'comece':

        print(data)

        arq=open('data/file.zip','rb')
        for i in arq:
            conn.send(i)
    
        arq.close()

        time.sleep(1)
        conn.sendall(bytes('terminei', 'utf-8'))

conn.close()