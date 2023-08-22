import sys
from socket import *
from time import sleep
import threading
import pickle

serverIP = '10.0.0.3'
serverPort = 10080
clientPort = 10081

def send_thread(sock):
    while True:
        sock.sendto(("register "+clientID).encode(),(serverIP,serverPort))
        sleep(10)
        
def recv_thread(sock,clientList):
    while(True):
        data,addr = sock.recvfrom(512)
        msg=data.decode().split(" ")
        if msg[0] == "list":
            data,addr = sock.recvfrom(512)
            clientList[:]=pickle.loads(data)
        elif msg[0] == "append":
            data,addr = sock.recvfrom(512)
            clientList.append(pickle.loads(data))
        elif msg[0] == "del":
            clientList[:] = [client for client in clientList if client[0]!=msg[1]]
        elif msg[0] == "From":
            print(msg[0]+" "+msg[1]+" ["+' '.join(msg[2:])+"]")
            

def client(serverIP, serverPort, clientID):
    """
    Write your code!!!
    """

    clientList = []
    
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind(('',clientPort))
    receiving = threading.Thread(target=recv_thread,args=(sock,clientList))
    receiving.daemon = True
    receiving.start()
    sending = threading.Thread(target=send_thread,args=(sock,))
    sending.daemon = True
    sending.start()
    
    while True:
        commands = input("").split(" ")
        if commands[0] == '@show_list':
            for client in clientList:
                print(client[0]+" "+client[1][0]+":"+str(client[1][1]))
        elif commands[0] == '@chat':
            for client in clientList:
                if client[0] == commands[1]:
                    sock.sendto(("From "+clientID+" "+' '.join(commands[2:])).encode(),client[1])
        elif commands[0] == '@exit':
            sock.sendto(("deregister "+clientID).encode(),(serverIP,serverPort))
            sys.exit(0)
    pass


"""
Don't touch the code below!
"""
if  __name__ == '__main__':
    clientID = input("")
    client(serverIP, serverPort, clientID)


