import socket


def client_program():
    ClientMultiSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.SOCK_STREAM)
    
    host = '192.168.1.9'
    port = 2004
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    res = ClientMultiSocket.recv(1024)
    while True:
        Input = input('Hey there: ')
        ClientMultiSocket.send(str.encode(Input))
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))
    ClientMultiSocket.close()

# Make function search for server


   
    


if __name__ == '__main__':
    client_program()