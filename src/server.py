import socket
import json
from _thread import *
import threading
import random


class Server:
    def setup(self):
        self.ServerSideSocket = socket.socket()
        self.host = '192.168.1.9'
        self.port = 2004
        self.ThreadCount = 0
        self.clients = []
        self.responses_categories = {}
        self.dicionario = {}
        self.responses = []
        self.invalid_responses={}
        self.invalid_responses_received_count = 0

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

            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.multi_threaded_client, (Client, ))

        self.ServerSideSocket.close()

    def find_client(self, connection):
        for client in self.dicionario.items():
            if (client[1] == connection):
                return client[0]

    def multi_threaded_client(self, connection):

        connection.send(str.encode(json.dumps(
            {"length": 128, "data": {"type": "connection_established"}})))
        while True:
            try:
                self.data = connection.recv(2048).decode('utf-8')
                if (self.data):
                    obj = json.loads(self.data)
                    tipo = obj["data"]["type"]
                    if (tipo == "find_server"):
                        self.client.send(str.encode("server_found"))
                    elif (tipo == "send_name"):
                        if obj["data"]["name"] in self.dicionario:
                            response = {
                                "length": 2048,
                                "data": {
                                    "type": "name_already_exists",
                                    "value": True,
                                }
                            }
                            connection.send((json.dumps(response).encode('utf-8')))
                        else:
                            self.dicionario.update(
                                {obj["data"]["name"]: connection})
                            self.clients.append(connection)
                            response = {
                                "length": 2048,
                                "data": {
                                    "type": "name_already_exists",
                                    "value": False,
                                }
                            }
                            connection.send((json.dumps(response).encode('utf-8')))
                        for client in self.clients:
                            response = {
                                "length": 32,
                                "data": {
                                    "type": "verify_number_of_players",
                                    "number_of_players": len(self.clients),
                                }
                            }
                            client.send((json.dumps(response).encode('utf-8')))

                    elif (tipo == "stop"):
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
                    elif (tipo == "response"):
                        self.responses.append(obj["data"])
                        if (len(self.responses) == len(self.clients)):
                            
                            self.split_responses_in_groups()
                            response = {
                                "length": 4096,
                                "data": {
                                    "type": "validate_response",
                                    "responses": self.responses_categories,
                                }
                            }
                            for client in self.clients:
                                client.send((json.dumps(response).encode('utf-8')))



                    elif (tipo == "verify_number_of_players"):
                        response = {
                            "length": 32,
                            "data": {
                                "type": "verify_number_of_players",
                                "number_of_players": len(self.clients),
                            }
                        }
                        connection.send((json.dumps(response).encode('utf-8')))
                    elif (tipo == "start_game"):
                        letter = self.random_letters()
                        for client in self.clients:
                            response = {
                                "data": {
                                    "type": "start_game",
                                    "letter": letter,
                                }
                            }
                            client.send((json.dumps(response).encode('utf-8')))
                    
                    elif(tipo == "invalid_responses"):
                        print(obj["data"]["responses"])
                        self.invalid_responses_received_count+=1
                        received_invalid_responses = obj["data"]["responses"]
                        for key in received_invalid_responses:
                            self.invalid_responses[key].extend(received_invalid_responses[key])


                        if(self.invalid_responses_received_count == len(self.clients)):
                            rank = self.score()
                            response = {
                                "data":{
                                    "type":"score",
                                    "ranking": rank
                                }
                            }
                            for client in self.clients:
                                client.send((json.dumps(response).encode('utf-8')))
                    
            except Exception as e:
                print(e)
                break
                

        connection.close()

    # def send_all_clients(self, message):
    #     for client in self.clients:
    #         client.send((json.dumps(message).encode('utf-8')))

    def random_letters(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        # select one letter from the list
        return random.choice(letters)

    def verify_connections(self):
        for client in self.clients:
            client.send(str.encode(json.dumps(
                {"length": 2048, "data": {"type": "verify_connections"}})))
            self.data = client.recv(2048).decode('utf-8')
            if (self.data):
                obj = json.loads(self.data)
                tipo = obj["data"]["type"]
                if (tipo == "verify_connections"):
                    print("conectado")
                else:
                    print("desconectado")
                    self.clients.remove(client)
                    self.dicionario.pop(self.find_client(client))
                    print(self.dicionario)
                    print(self.clients)

    def split_responses_in_groups(self):

        inputs = []

        for i in range(0, len(self.responses)):
            inputs.extend(self.responses[i]["inputs"])

        for input in inputs:
            if input["name"] in self.responses_categories.keys():
                self.responses_categories[input["name"]].append(input["value"])
            else:
                self.responses_categories[input["name"]] = [input["value"]]
        
        # add responses_categories keys to invalid_responses
        for key in self.responses_categories.keys():
                self.invalid_responses[key] = []
        

    def score(self):
        ranking = []
        for key in self.invalid_responses:
            values = self.invalid_responses[key]
            for value in values:
                cont = 0
                for i in range(0, len(values)):
                    if value == values[i]:
                        cont += 1
                if cont < int(len(self.clients)/2):
                    self.invalid_responses[key].remove(value)
                else:
                    self.invalid_responses[key].remove(value)

        for response in self.responses:
            score = 0
            for input in response["inputs"]:
                if input["value"] in self.invalid_responses[input["name"]]:
                    score -= 1
                else:
                    score+= 1
            
            ranking.append({"name": response["name"], "score": score})
        
        ranking = sorted(ranking, key=lambda k: k['score'], reverse=False)
        return ranking
        
    
                        
                   
            # verify if in the dictionary[key] there is a value repeated
            

      
      

       



    def __init__(self):
        self.setup()


if __name__ == "__main__":
    main = Server()
