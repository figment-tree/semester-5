import socket as s

REQUEST_PORT = 10000
MAX_SIZE = 2000

# creates a new TCP socket
Client = s.socket(s.AF_INET, s.SOCK_STREAM)
# bind socket to localhost over the requested port number
Client.connect(('localhost', REQUEST_PORT))

msgToServer = "Hello server!"
# Message is encoded in utf-8, since the send() function 
# expects data in bytes and not as a string
Client.sendall(msgToServer.encode('utf-8'))

msg = Client.recv(MAX_SIZE)

print(msg)

Client.close()
