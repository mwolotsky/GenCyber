'''
Created on Jul 20, 2016

@author: Max
'''

from WebLibs import host, accept, exists, send, readAll

def getRequest(CLIENT):
    #Receive Request from Client
    data = CLIENT.recv(1024)
    #Separate the received string into an array
    #Separates by spaces by default, can pass in other characters to separate by
    split = data.split()
    #If the request is a valid GET request
    if split[0] == "GET":
        #If only / is given, assume /index.html by default
        if split[1] == "/":
            return "/index.html"
        #Otherwise use the full path
        else:
            return split[1]
    #Return 400 Error if invalid GET request
    return "/400.html"

WEB_ROOT = "www"
IP = #ENTER IP ADDRESS HERE
PORT = #ENTER PORT NUMBER HERE

host = host(IP, PORT)

while True:
    #ENTER CONNECTION INFORMATION
    if exists(WEB_ROOT + path):
        #IF THE FILE EXISTS DO THIS
    else:
        #IF THE FILE DOESN'T EXIST DO THIS
    #SEND A RESPONSE


