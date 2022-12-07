import socket
import json
import threading
import netifaces as ni



class Client():
    def __init__(self):
        self.stop = False
        self.host = '192.168.1.9'
        self.port = 2004
        self.name = ""
        self.nameRequesterStop = ""
        self.ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(ni.gateways()['default'][ni.AF_INET][0])
        self.run()
    
    def run(self):
        print('Waiting for connection response')
        try:
            self.ClientMultiSocket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))
        print('Connected')
        threading.Thread(target=self.thread).start()
    
    def envia_mensagem(self, mensagem):
        self.ClientMultiSocket.send(str.encode(mensagem))
    
    def thread(self):
        while True:
            res = self.ClientMultiSocket.recv(2048).decode('utf-8')

            try:
                res = self.ClientMultiSocket.recv(2048).decode('utf-8')
                if(res):
                    response = json.loads(res)
                    if(response["data"]["type"]=="response"):
                        self.stop = True
                        self.nameRequesterStop = response["data"]["name_request_stop"]
               
            except:
                
                print("Connection closed")
                break
        

    def destroy(self):
        self.ClientMultiSocket.shutdown(socket.SHUT_RDWR)
        self.ClientMultiSocket.close()

    def find_server(self):
        for i in range(1, 255):
            self.host = '192.168.1.' + str(i)
            #Enviar uma mensagem com o tipo: "find_server" para o servidor, aguardar resposta == "server_found"

  

        


        # self.ClientMultiSocket.close()

# Make function search for server


