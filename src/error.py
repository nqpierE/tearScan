class Error:
    flag: bool = False
    message: str = ""

    def __init__(self, flag, message):
        self.flag = flag
        self.message = message
