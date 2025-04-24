class Debug:
    def __init__(self, logfile: str, chatlog: bool) -> None:
        self.logfile = logfile
        self.chatlog = chatlog

    def log(self, msg) -> None:
        if self.chatlog: print(msg)
        with open(self.logfile, "a", encoding="utf-8") as file: file.write(f"{msg}\n")

    def clearlog(self):
        with open(self.logfile, "w", encoding="utf-8") as file: file.write("")
