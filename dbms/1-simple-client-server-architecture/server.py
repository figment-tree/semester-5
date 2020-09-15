import socket as s

REQUEST_PORT = 10000
MAX_SIZE = 2000

# creates a new TCP socket
Server = s.socket(s.AF_INET, s.SOCK_STREAM)
# bind socket to localhost over the requested port number
Server.bind(('localhost', REQUEST_PORT))

# the listen() function tells the socket that it is a SERVER socket
# tells the queue up a maximum of 5 connection requests if
# multiple clients try to connect
Server.listen(5)

# continuously listens for client connection requests
while True:
    # accept client connection from outside to create client socket
    (NewClient, address) = Server.accept()

    msg = NewClient.recv(MAX_SIZE)
    # when msg is 0 bytes, it means the client has closed the connection
    if msg != '':
        print("Received message from client: {msg}".format(msg=msg))

        msgToClient = "Hello client!"
        # Message is encoded in utf-8, since the send() function
        # expects data in bytes and not as a string
        NewClient.sendall(msgToClient.encode('utf-8'))

        NewClient.close()
