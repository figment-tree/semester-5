import socket as s
import threading
import sys
import time
from random import randint
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


REQUEST_PORT1 = 10000
REQUEST_PORT2 = 8080
MAX_SIZE = 2000


class Server:
    connections = []
    peers = []

    def __init__(self):
        # creates a new TCP socket
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)

        # bind socket to localhost over the requested port number
        try:
            sock.bind(('localhost', REQUEST_PORT1))
        except s.error:
            sock.bind(('localhost', REQUEST_PORT2))

        # the listen() function tells the socket that it is a SERVER socket
        # tells the queue up a maximum of 5 connection requests if
        # multiple peers try to connect
        sock.listen(5)
        logging.info("Serving now...")

        while True:
            # accept peer connection from outside to create client socket
            (NewPeer, address) = sock.accept()

            peerThread = threading.Thread(
                target=self.handler,
                args=(NewPeer, address))
            peerThread.daemon = True
            peerThread.start()

            self.connections.append(NewPeer)
            self.peers.append(address[0])
            logging.info("{}:{} connected.".format(address[0], address[1]))
            self.sendPeers()

    def handler(self, NewPeer, address):
        try:
            # continuously listens for peer connection requests
            while True:
                msg = NewPeer.recv(MAX_SIZE)

                for connection in self.connections:
                    connection.send("{peer} says: {message}".format(
                        peer=address[1],
                        message=msg.decode("utf-8")).encode("utf-8"))

                # when msg is 0 bytes, it means the peer
                # has closed the connection
                if msg == '':
                    logging.info("{}:{} disconnected.".format(
                        address[0], address[1]))
                    self.connections.remove(NewPeer)
                    self.peers.remove(address[0])
                    NewPeer.close()
                    self.sendPeers()
                    break
        except BrokenPipeError:
            logging.info("{}:{} disconnected.".format(
                address[0], address[1]))

    def sendPeers(self):
        peersStr = ""
        for peer in self.peers:
            peersStr = peersStr + peer + ","

        for connection in self.connections:
            connection.send(b"\x11" + peersStr.encode("utf-8"))


class Client:
    def sendMsg(self, sock):
        while True:
            msg = str(input(""))
            sock.send(msg.encode("utf-8"))

    def __init__(self, address='localhost'):
        # creates a new TCP socket
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        # connect socket to localhost over the requested port number
        try:
            sock.connect((address, REQUEST_PORT1))
        except s.error:
            sock.connect((address, REQUEST_PORT2))
        logging.info("Connected to peer network.")

        iThread = threading.Thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            msg = sock.recv(MAX_SIZE)
            if not msg:
                break
            if msg[0:1] == b"\x11":
                self.updatePeers(msg[1:])
            else:
                logging.info(msg.decode("utf-8"))

    def updatePeers(self, peerData):
        p2p.peers = peerData.decode("utf-8").split(",")[:-1]


class p2p:
    peers = ['localhost']   # localhost is default peer


if __name__ == "__main__":
    # The new peer can either act as a client or as a server
    # within the peer network. If a peer is currently serving
    # data, this new one acts as a client, and if no peer is
    # sharing data, the new peer acts as the server.
    while True:
        try:
            logging.info("Trying to connect...")
            time.sleep(randint(1, 5))

            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                try:
                    server = Server()
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    logging.debug("Couldn't start server...")
        except KeyboardInterrupt:
            sys.exit(0)
