import socket
import sys
from thread import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player1 = None
player2 = None

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        if not data: 
            break
        #send data to the other player
     	if conn == player1
        	player2.sendall(reply)
        if conn == player2
        	player2.sendall(reply)

     
    #came out of loop
    conn.close()


#wait to accept a connection - blocking call
conn, addr = s.accept()
player1 = conn
print("Player one connected")

conn, addr = s.accept()
player2 = conn
print("Player one connected")
#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
start_new_thread(clientthread ,(player1,))
start_new_thread(clientthread ,(player2,))

#to keep the threads alive, is this necessary?
while 1
	pass
 
s.close()