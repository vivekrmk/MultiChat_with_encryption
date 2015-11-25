import socket
import threading
import time
#from cryptography.fernet import Fernet
from Crypto.Cipher import AES

shutdown = False
  
def receiving(name,sock):
			  #print "Client"
			  while 1:
			    try:
				from cryptography.fernet import Fernet
				from Crypto.Cipher import AES
				#while true:
				data, addr = sock.recvfrom(2048)      # returns string and address from source.
				# Decryption
				#print data
				decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
				# print data + "suite obj active" 
				#print data + "---->this is the encrypted form \n"
				plain_text = decryption_suite.decrypt((data))
				#f = Fernet('UN_CY-VmhvnvG28OPJSKr7k4CrJyIfQeJuyuvhAIWOg=')
				#plain_text = f.decrypt(data)
				 
				print time.ctime(time.time()) +"::" + plain_text
				
				
			    except:
				pass
			      
			    finally:
				pass
				    #tlock.release()           # end of critical section.
			      
host='localhost'  #to be changed.
port=0
server=(host,6000)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #using IPV4, UDP.
s.bind((host,port))   #s.bind takes one argument address.
#s.setblocking(0)  # going to accept all connection requests.
rt = threading.Thread(target = receiving,args = ("recvthread", s))  # passing the initialised socket to thread.
rt.start()    #start thread

alias = raw_input("\n\nName: ")
message= raw_input(alias + "-> ")
s.sendto(alias + "::" + message, server)
while message !=  'q' :
	if message != '' :
	  message = raw_input()
	  message = alias + ":" + message
	
	# Encryption
	encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	cipher_text = encryption_suite.encrypt(message.ljust(32))
	# s.sendto(alias + "::" + message, server)     #if u want to send plain text.
	#f = Fernet('UN_CY-VmhvnvG28OPJSKr7k4CrJyIfQeJuyuvhAIWOg=')   #predetermined key
	#token = f.encrypt(message)

	s.sendto(cipher_text,server)  #sending encrypted message to server.
	#s.sendto(alias + "::" + token,server)  #sending encrypted message to server.
        #print data   
      
	      
	    
	
        
	
	
shutdown = True
rt.join()
s.close()

  