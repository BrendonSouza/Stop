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
        self.number_of_players = 0
        self.responsesForValidate = {}        
        self.ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name_already_exists = False
        self.ranking = []
        self.sorted_letter= ''
        self.start_game = False
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
            try:
                res = self.ClientMultiSocket.recv(2048).decode('utf-8')
                if(res):
                    response = json.loads(res)

                    if(response["data"]["type"]=="response"):
                        self.stop = True
                        self.nameRequesterStop = response["data"]["name_request_stop"]
                    elif(response["data"]["type"]=="verify_number_of_players"):
                        self.number_of_players = response["data"]["number_of_players"]
                       
                    elif(response["data"]["type"]=="name_already_exists"):
                        self.name_already_exists = response["data"]["value"]
                        
                    elif(response["data"]["type"]=="validate_response"):
                        self.responsesForValidate = response["data"]["responses"]
                    elif(response["data"]["type"]=="score"):
                        self.ranking = response["data"]["ranking"]
                    elif(response["data"]["type"]=="start_game"):
                        self.start_game = True
                        self.sorted_letter = response["data"]["letter"]
     
            except Exception as e:

                print(e)
                print("Connection closed")
                break
        

    def destroy(self):
        self.ClientMultiSocket.shutdown(socket.SHUT_RDWR)
        self.ClientMultiSocket.close()

    def find_server(self):
        for i in range(1, 255):
            self.host = '192.168.1.' + str(i)
            try:
                self.ClientMultiSocket.connect((self.host, self.port))
                self.ClientMultiSocket.send(str.encode(json.dumps({"length": 2048, "data": {"type": "find_server"}})))
                res = self.ClientMultiSocket.recv(2048).decode('utf-8')
                if(res):
                    response = json.loads(res)
                    if(response["data"]=="server_found"):
                        print("Server found")
                        self.ClientMultiSocket.send(str.encode(json.dumps({"length": 2048, "data": {"type": "send_name", "name": self.name}})))
                        break;
            except Exception as e:
                
                print("não há servidor na rede")
                continue
            #Enviar uma mensagem com o tipo: "find_server" para o servidor, aguardar resposta == "server_found"

  

        


        # self.ClientMultiSocket.close()

# Make function search for server


