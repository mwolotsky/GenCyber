import sys
import socket
import os
URL = sys.argv[1]

L1 = URL.split("/")
L2 = L1[0].split(":") + L1[1:]

host = L2[0]
port = L2[1]
path = "/" + "/".join(L2[2:])
if host == "localhost" or len(host.split(".")) == 4:
	try:
		if int(port) >= 0 and int(port) < 2 **16:
			pass
	except:
		print "Error in URL Format"
		exit()
else:
	print "Error in URL Format"
	exit()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,int(port)))
s.send("GET %s" % path)
answer = s.recv(1024)
s.close()

file = open(".tempfile",'w')
file.write(answer)
file.close()

os.system("iceweasel .tempfile")
