'''
Created on Jul 20, 2016

@author: Max
'''
import socket
import os

def connect(IP,PORT):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))
    return s

def host(IP,PORT):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((IP,PORT))
    s.listen(5)
    return s

def exists(path):
    return os.path.exists(path)

def accept(SOCKET):
    client, _address = SOCKET.accept()
    return client

def close(CLIENT):
    CLIENT.close()

def readAll(filename):
    file = open(filename,'r')
    Str = file.read()
    file.close()
    return Str
   
def getRequest(CLIENT):
    data = CLIENT.recv(1024)
    split = data.split()
    if split[0] == "GET":
        if split[1] == "/":
            return "/index.html"
        else:
            return split[1]
    return "/404.html"

def send(Str, SOCKET):
    SOCKET.send(Str)
    SOCKET.close()

def receive(SOCKET):
    resp = SOCKET.recv(1024)
    SOCKET.close()
    return resp

    