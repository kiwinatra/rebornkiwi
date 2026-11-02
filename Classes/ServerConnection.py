import socket

import Configuration
from Classes.Connection import Connection
from Classes.Logger import Logger


class ServerConnection:
    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if Configuration.settings["DisableNagle"] == True:
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        Logger.info("NET", f"Listening on {address[0]}:{address[1]}")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            Logger.info("NET", f"Client connected {address[0]}:{address[1]}")
            Connection(socket, address).start()
