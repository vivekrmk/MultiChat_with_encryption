import socket
import time


host = '127.0.0.1'
port = 6000
clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print host , port
s.bind((host ,port))

s.setblocking(0)
quitting= False

print "server started"
 
while not quitting : 
    try : 
	  data, addr = s.recvfrom(1024)
	  if "quit" in str(data):
	           quitting = True
	  if addr not in clients:
	          clients.append(addr)
	          
	  print time.ctime(time.time()) +"::" + str(data) 
	 
	  for client in clients:
	    if addr != client:
	     s.sendto(data,client)
	    print client
    except :
         pass
       
s.close()
    
    
	          