import socket as s
import subprocess as sp
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

REQUEST_PORT_1 = 10000
REQUEST_PORT_2 = 8080
MAX_SIZE = 2000

# creates a new TCP socket
Server = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    # bind socket to localhost over the requested port number
    Server.bind(('localhost', REQUEST_PORT_1))
except OSError:
    Server.bind(('localhost', REQUEST_PORT_2))

# the listen() function tells the socket that it is a SERVER socket
# tells the queue up a maximum of 5 connection requests if
# multiple clients try to connect
Server.listen(5)

# continuously listens for client connection requests
while True:
    # accept client connection from outside to create client socket
    (NewClient, address) = Server.accept()
    logging.info("Accepted connection request from a client.")

    databaseName = NewClient.recv(MAX_SIZE)

    # when msg is 0 bytes, it means the client has closed the connection
    if databaseName != '':
        logging.info("Received database name from client.")

        startSQL = "sudo mysql"
        sqlQuery = "use {db}; {clientQueries}".format(
            db=databaseName[:].decode("utf-8"),
            clientQueries=NewClient.recv(MAX_SIZE).decode("utf-8"))

        logging.info("Received query from client.")

        # spawn a new shell to open mysql
        sqlCMD = sp.Popen(startSQL,
                          shell=True,
                          stdin=sp.PIPE,
                          stdout=sp.PIPE)

        # send the queries to the subprocess pipe opened by
        # the previous line of code
        output = sqlCMD.communicate(sqlQuery.encode("utf-8"))[0].strip()
        NewClient.sendall(output)

        logging.info("Sent output of query to client.")

        NewClient.close()
