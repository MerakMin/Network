from socket import *

s_ip = 'localhost'
s_port = 12345
c_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)

c_sock.sendto('안녕, server!'.encode('utf-8'), (s_ip, s_port))

c_sock.close()