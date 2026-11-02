# DisableNagle: reduce delay and improve performance between client and server BUT require more power #

settings = {
    "DisableNagle": True,
    "PrintEnabled": True,
    "UseContentUpdater": False,
    "Proxy": False,
    "DumpPacket": False,
    "Blacklist": [24109],
    "DumpMajor": 44,

    # ---- Logging ----
    "LogLevel": "DEBUG",
    "LogToFile": True,
    "LogFile": "Logs/server.log",
    "LogColor": True,
    "LogTime": True,
    "LogPackets": True,
    "LogDatabase": True,
    "LogCommands": True,

    # ---- Event Rotation ----
    "EventRotation": [
        {"Mode": "Showdown",     "Count": 1},
        {"Mode": "DuoShowdown",  "Count": 1},
        {"Mode": "BrawlBall",    "Count": 1},
        {"Mode": "GemGrab",      "Count": 1},
        {"Mode": "KingOfHill",   "Count": 1},
        {"Mode": "Bounty",       "Count": 1},
        {"Mode": "Heist",        "Count": 1},
        {"Mode": "Knockout",     "Count": 1},
    ],
}
