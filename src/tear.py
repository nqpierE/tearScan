from src.error import Error
from requests import Request


class Tear:
    word_to_search: str = None
    start_point: str = None
    identical_domain_depth: int = None
    identical_domain_frequency: int = None
    entire_depth: int = None

    def __init__(self):
        self.identical_domain_depth = 3
        self.identical_domain_frequency = 1
        self.entire_depth = 10

    def __verify_props(self):
        if self.word_to_search == None or self.start_point == None or self.identical_domain_depth == None or self.identical_domain_frequency == None or self.entire_depth == None:
            message = ""
            error_flag: Error = Error(True, message)
            return error_flag
        else:
            error_flag: Error = Error(False, message)
            return error_flag

    def startTear(self):
        verify_result = self.__verify_props()
        if verify_result.flag:
            return verify_result
        else:
            pass
