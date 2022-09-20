from socket import *

s_ip = 'localhost'
s_port = 12345
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind((s_ip, s_port))

s_sock.settimeout(5)

data, c_addr = s_sock.recvfrom(1024)

print('Received from', c_addr)
print('Obtained ', data.decode('utf-8'))

s_sock.close()