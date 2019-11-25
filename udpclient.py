import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = raw_input()
client.sendto(data, ("127.0.0.1", 8000))
data, addr = client.recvfrom(1024)
print data
client.close()
