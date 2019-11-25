import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", 8000)
server.bind(address)
while True:
    data, address = server.recvfrom(1024)
    t = time.localtime()
    response = time.asctime(t) + "\n" + data.upper()
    server.sendto(response, address)
server.close()
