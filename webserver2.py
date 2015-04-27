#import socket module
import socket

#CREATE MAIN THREAD
print socket.gethostbyname(socket.getfqdn())
host =  socket.gethostbyname(socket.gethostname())
serverPort = 5555
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
#print socket.gethostbyname(socket.gethostname(host))

serverSocket.bind((host,serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print 'Ready to serve...\n'
	#CREATE TCP CONNECTION THROUGH ANOTHER PORT
	connectionSocket,addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(2048)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		#print outputdata
		#SEND one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for the file not found
		print '404 Not Found'
		connectionSocket.send('HTTP/1.1 404 Not Found\n')
		#Close clinet socket
		connectionSocket.close()
		
serverSocket.close()