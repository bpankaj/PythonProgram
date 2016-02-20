import socket
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serverSocket.bind((host, port))

serverSocket.listen(5)
while True:
	clientSocket, addr = serverSocket.accept()
	print ("Got a connection from %s" % str(addr))
	currentTime = time.ctime(time.time()) + "\r\n"
	clientSocket.send(currentTime.encode('ascii'))
	clientSocket.close()
