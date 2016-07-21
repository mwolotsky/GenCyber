import socket
import os

def readAll(filename):
    file = open(filename,'r')
    Str = file.read()
    file.close()
    return Str

WEB_ROOT = "www"

host = 'localhost'
port = 50000
backlog = 5
size = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while True:
    client, address = s.accept()
    data = client.recv(size)
    split = data.split()
    if split[0] == "GET":
        path = "/index.html" if split[1] == "/" else split[1]
        path = WEB_ROOT + path
        if os.path.exists(path):
            content = readAll(path)
            res = "HTTP/1.1 200 OK\r\n" + "Content-type: text/html\r\n" + "Content-length: %d" % len(content) + "\r\n" + "\r\n" + content
        else:
            content = readAll(WEB_ROOT + "/404.html")
            res = "HTTP/1.1 404 Not Found\r\n" + "Content-type: text/html\r\n" + "Content-length: %d" % len(content) + "\r\n" + "\r\n" + content
    client.send(res)
    client.close()


