import os
import sys
import datetime
import threading

import Configuration


class _Ansi:
    RESET = "\033[0m"
    GREY = "\033[90m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"


_LEVELS = {
    "DEBUG": 10,
    "INFO": 20,
    "WARN": 30,
    "ERROR": 40,
}

_LEVEL_COLORS = {
    "DEBUG": _Ansi.GREY,
    "INFO": _Ansi.GREEN,
    "WARN": _Ansi.YELLOW,
    "ERROR": _Ansi.RED,
}


class Logger:
    _lock = threading.Lock()
    _level = _LEVELS.get(Configuration.settings.get("LogLevel", "INFO").upper(), 20)
    _use_color = bool(Configuration.settings.get("LogColor", True)) and sys.stdout.isatty()
    _show_time = bool(Configuration.settings.get("LogTime", True))
    _log_to_file = bool(Configuration.settings.get("LogToFile", False))
    _log_file = Configuration.settings.get("LogFile", "Logs/server.log")

    @staticmethod
    def _ensure_log_dir():
        if not Logger._log_to_file:
            return
        directory = os.path.dirname(Logger._log_file)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok=True)
            except Exception:
                Logger._log_to_file = False

    @staticmethod
    def _write_to_file(line):
        if not Logger._log_to_file:
            return
        try:
            with Logger._lock:
                with open(Logger._log_file, "a", encoding="utf-8") as f:
                    f.write(line + "\n")
        except Exception:
            Logger._log_to_file = False

    @staticmethod
    def _format(level, category, message):
        parts = []
        if Logger._show_time:
            parts.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}]")
        parts.append(f"[{level:<5}]")
        if category:
            parts.append(f"[{category:<5}]")
        parts.append(str(message))
        return " ".join(parts)

    @staticmethod
    def _emit(level, category, message, color=None):
        if _LEVELS.get(level, 20) < Logger._level:
            return

        plain = Logger._format(level, category, message)

        if Logger._use_color:
            line_color = color or _LEVEL_COLORS.get(level, _Ansi.RESET)
            cat_color = _Ansi.CYAN
            if category:
                header = ""
                if Logger._show_time:
                    header += f"{_Ansi.GREY}[{datetime.datetime.now().strftime('%H:%M:%S')}]{_Ansi.RESET} "
                header += f"{line_color}[{level:<5}]{_Ansi.RESET} "
                header += f"{cat_color}[{category:<5}]{_Ansi.RESET} "
                print(header + str(message), flush=True)
            else:
                print(f"{line_color}{plain}{_Ansi.RESET}", flush=True)
        else:
            print(plain, flush=True)

        Logger._write_to_file(plain)

    # ---- Public API ----

    @staticmethod
    def debug(category, message):
        Logger._emit("DEBUG", category, message)

    @staticmethod
    def info(category, message):
        Logger._emit("INFO", category, message)

    @staticmethod
    def warn(category, message):
        Logger._emit("WARN", category, message)

    @staticmethod
    def error(category, message):
        Logger._emit("ERROR", category, message)

    @staticmethod
    def packet(direction, message_type, name, size):
        """
        direction: 'in' — клиент → сервер (стрелка →),
                   'out' — сервер → клиент (стрелка ←)
        """
        if not Configuration.settings.get("LogPackets", True):
            return
        arrow = "→" if direction == "in" else "←"
        color = _Ansi.MAGENTA if direction == "in" else _Ansi.CYAN
        text = f"{arrow} {message_type:<6} {name} ({size} B)"
        Logger._emit("DEBUG", "PKT", text, color=color)


Logger._ensure_log_dir()
