import sys
from time import sleep
from socket import *
import pickle
import threading

serverPort = 10080
def check_alive(clientList,clientID,addr,sock):
    ClientIDs = [client[0] for client in clientList]
    del clientList[ClientIDs.index(clientID)]
    for client in clientList:
        sock.sendto(("del "+clientID).encode(),client[1])
    print(clientID+" is disappeared "+str(addr[0])+":"+str(addr[1]))
    return

def server():
    """
    Write your code!!!
    """
    clientList = []
    timerDict = {}
    
    sock=socket(AF_INET,SOCK_DGRAM)
    sock.bind(('0.0.0.0',serverPort))
    
    while(True):
        data,addr = sock.recvfrom(512)
        msg = data.decode().split(" ")
        req = msg[0]
        clientID = msg[1]
        if req == "register":
            ClientIDs = [client[0] for client in clientList]
            if clientID in ClientIDs:
                timerDict.get(clientID).cancel()
                timer = threading.Timer(30,check_alive,args=(clientList,clientID,addr,sock,))
                timer.daemon = True
                timerDict[clientID] = timer
                timer.start()
            else:
                clientList.append([clientID,addr])
                timer = threading.Timer(30,check_alive,args=(clientList,clientID,addr,sock,))
                timer.daemon = True
                timerDict[clientID] = timer
                timer.start()
                for client in clientList:
                    if client[0] == clientID:
                        sock.sendto("list".encode(),client[1])
                        sock.sendto(pickle.dumps(clientList),client[1])
                    else:
                        sock.sendto("append".encode(),client[1])
                        sock.sendto(pickle.dumps([clientID,addr]),client[1])
                print(clientID+" "+addr[0]+":"+str(addr[1]))
        elif req == "deregister":
            timerDict.get(clientID).cancel()
            # clientList = [client for client in clientList if client[0]!=clientID]
            ClientIDs = [client[0] for client in clientList]
            del clientList[ClientIDs.index(clientID)]
            for client in clientList:
                sock.sendto(("del "+clientID).encode(),client[1])
            print(clientID+" is deregistered "+addr[0]+":"+str(addr[1]))
    pass


"""
Don't touch the code below
"""
if  __name__ == '__main__':
    server()


