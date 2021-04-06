from socket import *
 serverIP = ’servername’ 
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_STREAM) 
sentence = raw_input(‘Input lowercase sentence:’) 
clientSocket.connect((serverIP,serverPort)) 
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print ‘From Server:’, modifiedSentence 
clientSocket.close()
