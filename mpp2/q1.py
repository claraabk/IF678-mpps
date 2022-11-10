import socket

protocols = {'FTP': 21, 'SSH': 22, 'Telnet': 23, 'WHOIS': 43, 'DNS': 53, 'HTTP': 80, 'Skype': 81, 'POP3': 110, 'HTTPS': 443, 'VMWare Server Console': 902, 'Kazaa': 1214, 'Microsoft SQL Monitor': 1434, 'Windows Live Messenger': 1863, 'UPnP': 5000, 'VNC remote desktop protocol': 5500}
host = socket.gethostbyname('smtp.cin.ufpe.br')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

for protocol in protocols:

    if s.connect_ex((host, protocols[protocol])) == 0:
        print(f"Protocolo: {protocol} | Porta: {protocols[protocol]} - ABERTA")
        s.close()

    else:
        print(f"Protocolo: {protocol} | Porta: {protocols[protocol]} - FECHADA")
        s.close