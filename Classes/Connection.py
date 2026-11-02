import cProfile, pstats, sys
import time
import threading
import traceback

import Configuration
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Player import Player
from Classes.Logger import Logger
from Classes.MessageManager import MessageManager
from Classes.Messaging import Messaging
from Classes.Utility import Utility


class Connection(threading.Thread):
    def __init__(self, socket, address):
        super().__init__()
        self.client = socket
        self.address = address
        self.player = Player()
        self.timeout = time.time()

    def recv(self, n):
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                return b''
            data.extend(packet)
        return data

    def run(self):
        try:
            while True:
                time.sleep(0.001)
                messageHeader = self.client.recv(7)
                if len(messageHeader) >= 7:
                    headerData = Messaging.readHeader(messageHeader)
                    self.timeout = time.time()
                    packetPayload = Connection.recv(self, headerData[1])
                    if Configuration.settings["DumpPacket"] == True:
                        Utility.dumpPacket(packetPayload, headerData[0])
                    from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
                    Logger.packet("in", headerData[0], LogicLaserMessageFactory.getMessageName(headerData[0]), headerData[1])
                    MessageManager.receiveMessage(self, headerData[0], packetPayload)

                if time.time() - self.timeout > 7:
                    Logger.info("NET", f"Client {self.address[0]}:{self.address[1]} disconnected (timeout)")
                    allSockets = ClientsManager.GetAll()
                    if self.player.ID[1] in allSockets.keys() and allSockets[self.player.ID[1]]["Socket"] == self.client:
                        ClientsManager.RemovePlayer(self.player.ID)
                    self.client.close()
                    break

        except ConnectionError:
            Logger.info("NET", f"Client {self.address[0]}:{self.address[1]} disconnected")
            allSockets = ClientsManager.GetAll()
            if self.player.ID[1] in allSockets.keys() and allSockets[self.player.ID[1]]["Socket"] == self.client:
                ClientsManager.RemovePlayer(self.player.ID)
            self.client.close()

        except Exception:
            Logger.error("NET", traceback.format_exc())
