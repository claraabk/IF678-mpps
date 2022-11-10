from asyncore import read
import socket, select, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 48247))
s.listen(1)

conn, addr = s.accept()

#FUNÇÃO VERIFICAÇÃO TEMPO(X)
#0-15 SEG: PRINTA X
#15-20: TEM ALGUEM AÍ
#20+: WHILE = 0

while 1:
    #MENSAGEM CLIENTE
    #VERIFCAÇÃO TEMPO
    #MENSAGEM SERVIDOR
    #VERIFCAÇÃO TEMPO

    # print('testeeee')
    # conn.setblocking(0)
    ready = select.select([conn], [], [], 15)
    
    if ready[0] :
        data = conn.recv(1024)
        print(data)

        # conn.setblocking(0)
        thrdReady = select.select([sys.stdin], [], [], 15)

        if thrdReady[0]:
            conn.sendall(bytes(sys.stdin.readline().strip(), 'utf-8'))
        else:
            data = conn.recv(1024)
            print(data)

            frthReady = select.select([sys.stdin], [], [], 5)

            if frthReady[0]:
                conn.sendall(bytes(sys.stdin.readline().strip(), 'utf-8'))
            else:
                data = conn.recv(1024)
                print(data)

    else:
        conn.sendall(bytes('Tem alguem ai?', 'utf-8'))

        # conn.setblocking(0)
        scndReady = select.select([conn], [], [], 5)

        if scndReady[0]:
            data = conn.recv(1024)
            print(data)
            conn.sendall(bytes('To ligado!', 'utf-8'))
    
        else:
            conn.sendall(bytes('Fui!', 'utf-8'))
            break

conn.close()