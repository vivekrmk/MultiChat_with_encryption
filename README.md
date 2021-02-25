# MultiChat_with_encryption
This is a Client server encryption project that uses AES algorithm to encrypt messages on the wire.  While the multi- chat implmentation is patchy, The actual intention of this code was to check out the AES encryption on wire via the WIRESHARK tool.

 (Platform - Python): 
Implemented a secure chat application between two clients via a server. 
As the encrypted message traffic would be routed via server,
the server would note the time stamp of the message and the user. 
Only the end clients and the server can read the message(pre shared key) which was encrypted with AES Algorithm. 

for compiling and executing:
Python server.py

on an 2 other terminals for client 1 and client 2:
Python chatclient_encrypt.py

Enter your name in the terminal, enter the message, after the second message the routing will happen between clients via sever. The first message after the name is not routed(I have to still implement a database of clients for this-for logging etc, I have to complete this part...)

