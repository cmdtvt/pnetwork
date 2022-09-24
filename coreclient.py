import socket
import onlineUtilities
import time
import threading
import warnings

ip = "127.0.0.1"
port = 25565


import core

class Client(core.ComCore):
    def __init__(self,host='127.0.0.1',port=25565,bufferSize=1024):
        super().__init__(host,port,bufferSize)
        self.socket.connect((self.host,self.port))
        self.packetDelay = 5


    def listen(self,):
        ###TODO: check if socket is still active.
        while True:
            try:
                time.sleep(self.packetDelay)
                data = self.socket.recv(self.bufferSize)
                print('Received', self.ou.decodePacket(data))
                self.processPacket(data,self.socket)

            except socket.error as e:
                if self.ou.checkNetworkError(e.errno):
                    print("Recieved command to shutdown")
                    break
    def connect(self,):
        while True:
            s = socket.socket()
            s.settimeout(5)
            try:
                self.socket.connect((self.host,self.port))
                p = self.ou.createPacket('handShake',{
                    'username' : 'dev',
                    'password' : 'test'
                })
                self.socket.send(p)
                print("Connected to server")
                break

            except socket.error as e:
                self.ou.checkNetworkError(e.errno)






if __name__ == '__main__':
    c = Client()
    #c.bindAction("disconnect",c.ActionDisconnectConnection)
    c.start()

    while True:
        print("client runs")
        time.sleep(10)
