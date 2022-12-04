import socket
class Server:
    def setup(self):

        self. host = socket.gethostbyname(socket.gethostname())
        self.port = 5000  # initiate port no above 1024
        print("Server is running in ip"+str(self.host) +":"+str(self.port))
        print(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        self.server_socket.bind((self.host, self.port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        self.server_socket.listen(2)
        self.conn, self.address = self.server_socket.accept()  # accept new connection
        print("Exec")
        print("Connection from: " + str(self.address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            self.data = self.conn.recv(1024).decode()
            if not self.data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            self.data = input(' -> ')
            self.conn.send(self.data.encode())  # send data to the client

        self.conn.close()  # close the connectio

    def __init__(self):
        self.setup()

if __name__ == "__main__":
    main = Server()