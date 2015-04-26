import socket
import sys
import threading
from socket import *

def connectSocket( connectionSocket, addr):
	soc = socket(AF_INET, SOCK_STREAM)
	soc.bind(('127.0.0.1',0))
	try:
		message = connectionSocket.recv(2048)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
				#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
				#Send response message for the file not found
		print '404 Not Found'
		connectionSocket.send('HTTP/1.1 404 Not Found\n')
				#Close client socket
		connectionSocket.close()
	soc.close()
		
def mainThread():
	print "inside mainThread\n"
	serverPort = 5555
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serverSocket.bind(('127.0.0.1', serverPort))
	
	serverSocket.listen(1)
	while True:
		print 'Ready to serve..\n'
		connectionSocket,addr = serverSocket.accept()	
		try: 
			t1 = threading.Thread(target = connectSocket, args=(connectionSocket,addr))
			t1.start()
			t1.join()
		except:
			print "Error: unable to start thread2"
	
	serverSocket.close()
		

try:
	t = threading.Thread(target = mainThread)
	t.start()
	t.join()

except:
	print "Error: unable to start thread1"
	
