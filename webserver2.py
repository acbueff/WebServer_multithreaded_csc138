#import socket module

from socket import *

serverPort = 5555
serverSocket = socket(AF_INET, STOCK_STREAM)

#Prepare a server socket

serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)

while True:
	#Establish the connection
	print 'Ready to serve...\n'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(2048)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		print outputdata
		#SEND one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK\n')
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata[i])):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
	except IOError:
		#Send response message for the file not found
		print '404 Not Found'
		connectionSocket.send('\HTTP/1.1 404 Not Found\n')
		#Close clinet socket
		connectionSocket.close()
		
	serverSocket.close()