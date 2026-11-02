from Classes.Logger import Logger


class Debugger:
    @staticmethod
    def error(message):
        Logger.error("DBG", message)

    @staticmethod
    def warning(message):
        Logger.warn("DBG", message)
