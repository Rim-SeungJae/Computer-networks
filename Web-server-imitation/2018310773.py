# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:14:43 2021

@author: dipreez
"""

import threading
from socket import *
        
def client_thread(connectionSocket):
    while True:
        try:
            req = connectionSocket.recv(4096)
        except ConnectionResetError:
            break
        if req == b'':
            break
        request_data = req.decode().split()
        request_file=request_data[1][1:]
        try:
            with open(request_file,'r') as f:
                content = f.read()
                connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
                connectionSocket.send('Connection: keep-alive\r\n'.encode())
                connectionSocket.send(('Content-Length: '+str(len(content))+'\r\n\r\n').encode())
                connectionSocket.send(content.encode())
        except FileNotFoundError:
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            connectionSocket.send(response.encode())
            connectionSocket.send('Connection: keep-alive\r\n'.encode())
            connectionSocket.send(('Content-Length: '+str(0)+'\r\n\r\n').encode())
            
        except UnicodeDecodeError:
            with open(request_file,'rb') as f:
                content = f.read()
                connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
                connectionSocket.send('Connection: keep-alive\r\n'.encode())
                connectionSocket.send(('Content-Length: '+str(len(content))+'\r\n\r\n').encode())
                connectionSocket.send(content)
    print("client disconnected")
    connectionSocket.close()


serverPort = 10080
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind( ('', serverPort) )
serverSocket.listen( 5 )
print( 'The TCP server is ready to receive.' )
while True:
    connectionSocket, addr = serverSocket.accept()
    ct=threading.Thread(target=client_thread,args=(connectionSocket,))
    ct.start()
    
serverSocket.close()