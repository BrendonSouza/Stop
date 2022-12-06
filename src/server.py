import socket
from _thread import *
import threading
class Server:
    def setup(self):
        self.ServerSideSocket = socket.socket()
        self.host = '192.168.1.9'
        self.port = 2004
        self.ThreadCount = 0
        self.clients=[]

        try:
            self.ServerSideSocket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))
        print('Socket is listening..')
        self.ServerSideSocket.listen(5)
        self.execute()
        
    def execute(self):
        while True:
            Client, address = self.ServerSideSocket.accept()
            self.clients.append(Client)
            # TODO: remove unused threads(threads that are not connected to any client or the client is disconnected)
            
            # self.clients.append(address[0])
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.multi_threaded_client, (Client, ))
            self.ThreadCount += 1
            print('Thread Number: ' + str(self.ThreadCount))
            
            
            # if(address[0] not in self.clients):
            #     self.clients.append(address[0])
            #     print('Connected to: ' + address[0] + ':' + str(address[1]))
            #     start_new_thread(self.multi_threaded_client, (Client, ))
            #     self.ThreadCount += 1
            #     print('Thread Number: ' + str(self.ThreadCount))
            # else:
            #     print("Client already connected")
                # find the thread that is connected to the client
                # and send the message to that thread
                #Client.send(str.encode("Client already connected"))
                


        self.ServerSideSocket.close()
    
    def multi_threaded_client(self,connection):
        connection.send(str.encode('Server is working:'))
        while True:
            self.data = connection.recv(2048)
            self.response = 'Server message: ' + self.data.decode('utf-8')
            self.find_thread()
            if not self.data:
                break
            if(self.data.decode('utf-8')=="stop"):
                # send to all clients that the game is over
                for client in self.clients:
                    client.send(str.encode("stop == true"))
                



                
            connection.sendall(str.encode(self.response))
        connection.close()

    def find_thread(self):
       print(threading.enumerate())
       


    def __init__(self):
        self.setup()

if __name__ == "__main__":
    main = Server()