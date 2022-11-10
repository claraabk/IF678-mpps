import socket, select, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 44321))
s.connect(('localhost', 48247))

frst = select.select([sys.stdin], [], [], 15)

if frst[0]:
    msg = input()
    s.sendall(bytes(msg, 'utf-8'))

while 1:
    #s.setblocking(0)
    ready = select.select([s], [], [], 15)
    
    if ready[0]:
        data = s.recv(1024)
        print(data)

        #s.setblocking(0)
        thrdReady = select.select([sys.stdin], [], [], 5)

        if thrdReady[0]:
            s.sendall(bytes(sys.stdin.readline().strip(), 'utf-8'))
        else:
            data = s.recv(1024)
            print(data)

            frthReady = select.select([sys.stdin], [], [], 5)

            if frthReady[0]:
                s.sendall(bytes(sys.stdin.readline().strip(), 'utf-8'))
            else:
                data = s.recv(1024)
                print(data)

    else:
        s.sendall(bytes('Tem alguem ai?', 'utf-8'))

        #s.setblocking(0)
        scndReady = select.select([s], [], [], 5)

        if scndReady[0]:
            data = s.recv(1024)
            print(data)
            s.sendall(bytes('To ligado!', 'utf-8'))
        else:
            s.sendall(bytes('Fui!', 'utf-8'))
            break

s.close()