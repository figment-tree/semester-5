import socket as s
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

REQUEST_PORT_1 = 10000
REQUEST_PORT_2 = 8080
MAX_SIZE = 5000

# creates a new TCP socket
Client = s.socket(s.AF_INET, s.SOCK_STREAM)

try:
    # bind socket to localhost over the requested port number
    Client.connect(('localhost', REQUEST_PORT_1))
    logging.info("Successfully established connection to the server.")
except OSError:
    Client.connect(('localhost', REQUEST_PORT_2))

databaseName = str.encode(input("Enter name of database to be used: "))

if len(databaseName) > 0:
    # Message is encoded in utf-8, since the send() function
    # expects data in bytes and not as a string
    Client.sendall(databaseName)

    sqlQuery = str.encode(
        input("Enter SQL query to be executed by the server:\n"))

    logging.info("Retrieving data from the server...\n")
    Client.sendall(sqlQuery)
    output = str(Client.recv(MAX_SIZE), "utf-8")

    print(output)

Client.close()
