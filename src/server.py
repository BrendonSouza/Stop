import socket
import json
from _thread import *
import threading
class Server:
    def setup(self):
        self.ServerSideSocket = socket.socket()
        self.host = '192.168.1.9'
        self.port = 2004
        self.ThreadCount = 0
        self.clients=[]
        self.dicionario = {}
        self.responses = []

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
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.multi_threaded_client, (Client, ))
                
        self.ServerSideSocket.close()
    

    def find_client(self, connection):
        for client in self.dicionario.items():
            if(client[1] == connection):
                return client[0]
      

    def multi_threaded_client(self,connection):
        
        connection.send(str.encode(json.dumps({"length": 2048, "data": {"type": "connection_established"}})))
        while True:
            self.data = connection.recv(2048).decode('utf-8')
            if(self.data):
                obj =  json.loads(self.data)
                tipo = obj["data"]["type"]
                if(tipo == "find_server"):
                    self.client.send(str.encode("server_found"))
                elif(tipo == "send_name"):
                    self.dicionario.update({obj["data"]["name"]:connection})
                    print(self.dicionario)
                elif(tipo == "stop"):
                    print("enviou")
                    for client in self.clients:
                        response = {
                            "length": 2048,
                            "data": {
                                "type": "response",
                                "stop": True,
                                "name_request_stop": self.find_client(connection),
                            }
                        }
                        client.send((json.dumps(response).encode('utf-8')))
                elif(tipo == "response"):
                    self.responses.append(obj["data"])
                    
        connection.close()            
       


    def __init__(self):
        self.setup()

if __name__ == "__main__":
    main = Server()