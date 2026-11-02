import time

from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Static.StaticData import StaticData


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience)
        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(800)

        for i in range(800):
            self.writeDataReference(29, i)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(999)
        self.writeVInt(999)

        self.writeVInt(5)

        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)
        self.writeVInt(999)

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        ShopData = StaticData.ShopData

        self.writeVInt(1 + len(ShopData["Offers"]))

        self.writeVInt(1)
        for i in range(1):
            self.writeVInt(3)
            self.writeVInt(0)
            self.writeDataReference(16, 67)
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeInt(0)
        self.writeString("OFFER")
        self.writeBoolean(False)
        self.writeString("offer_ramadan22")
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeDataReference(0)

        for i in ShopData["Offers"]:
            self.writeVInt(i["RewardsCount"])
            for reward in i["Rewards"]:
                self.writeVInt(reward["ItemType"])
                self.writeVInt(reward["Amount"])
                if reward["CsvID1"] != 0:
                    self.writeDataReference(reward["CsvID1"], reward["CsvID2"])
                else:
                    self.writeDataReference(0)
                self.writeVInt(reward["SkinID"])

            self.writeVInt(i["Currency"])
            self.writeVInt(i["Cost"])
            self.writeVInt(i["Time"])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(i["Claim"])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(i["DailyOffer"])
            self.writeVInt(i["OldPrice"])
            self.writeInt(0)
            if i["Text"] == "None":
                self.writeString()
            else:
                self.writeString(i["Text"])
            self.writeBoolean(False)
            if i["Background"] == "None":
                self.writeString()
            else:
                self.writeString(i["Background"])
            self.writeVInt(-1)
            self.writeBoolean(i["Processed"])
            self.writeVInt(i["TypeBenefit"])
            self.writeVInt(i["Benefit"])
            self.writeString()
            self.writeBoolean(i["OneTimeOffer"])
            self.writeBoolean(i["Claimed"])
            self.writeDataReference(0)
            self.writeDataReference(0)

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVInt(20)
        self.writeLong(2, 1)
        self.writeLong(3, 0)
        self.writeLong(4, 0)
        self.writeLong(6, 0)
        self.writeLong(7, 0)
        self.writeLong(8, 0)
        self.writeLong(9, 0)
        self.writeLong(10, 0)
        self.writeLong(12, 1)
        self.writeLong(14, 0)
        self.writeLong(15, 0)
        self.writeLong(16, 1)
        self.writeLong(17, 0)
        self.writeLong(18, 0)
        self.writeLong(19, 0)
        self.writeLong(20, 0)
        self.writeLong(21, 0)
        self.writeLong(22, 1)
        self.writeLong(23, 0)
        self.writeLong(24, 1)

        self.writeVInt(0)

        self.writeVInt(2)
        for i in range(11, 13):
            self.writeVInt(13)
            self.writeVInt(34500)
            self.writeBoolean(True)
            self.writeVInt(0)

            self.writeByte(2)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(4294967292)
            self.writeInt(4294967295)
            self.writeInt(511)
            self.writeInt(0)

        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25)

        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13)
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(20)
        self.writeVInt(21)
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)

        self.writeVInt(4) # Events

        eventIndex = 1
        for i in [5, 115, 568, 25]:
            self.writeVInt(-1)
            self.writeVInt(eventIndex)  # EventType
            self.writeVInt(0)  # EventsBeginCountdown
            self.writeVInt(51208)  # Timer
            self.writeVInt(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVInt(-1)  # GameModeVariation
            self.writeVInt(2)  # State
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # Modifiers
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            self.writeVInt(0)
            self.writeBoolean(False)  # Power League Data Array
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # ChronosTextEntry
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(-1)
            eventIndex += 1

        self.writeVInt(0) # Comming Events

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0) # ReleaseEntry

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000063)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 1)
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(47, 41381)
        self.writeLong(48, 41381)
        self.writeLong(50, 0)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0)  # Double Token Event
        self.writeLong(31, 0)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)
        self.writeLong(87, 1)

        self.writeVInt(0) # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(0) # NotificationFactory

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVInt(16)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(99999) # Club coins

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(5)
        self.writeVInt(0)
        self.writeVInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
