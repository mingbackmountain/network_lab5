import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',12345))

data = raw_input()
client.send(data)
print client.recv(1024)

client.close()
