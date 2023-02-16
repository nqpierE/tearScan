from .error import Error
from . import crawl


class Tear:
    word: str = None
    root_url: str = None
    identical_domain_depth: int = None
    identical_domain_frequency: int = None
    entire_depth: int = None

    def __init__(self):
        self.identical_domain_depth = 3
        self.identical_domain_frequency = 1
        self.entire_depth = 3

    def __verify_props(self):
        if self.word == None or self.root_url == None or self.identical_domain_depth == None or self.identical_domain_frequency == None or self.entire_depth == None:
            message = ""
            error_flag: Error = Error(True, message)
            return error_flag
        else:
            message = ""
            error_flag: Error = Error(False, message)
            return error_flag

    def startTear(self):
        verify_result = self.__verify_props()
        if verify_result.flag:
            return verify_result
        else:
            including_url_list: list[str] = []
            trying_url_list: list[str] = [self.root_url]
            entire_url_list: list[str] = []
            identical_domain_list: list[str] = []
            for i in range(self.entire_depth):
                next_url_list: list[str] = []
                for j in range(len(trying_url_list)):
                    domain = trying_url_list[j].split("/")[2]
                    if identical_domain_list.count(domain) > self.identical_domain_depth:
                        break
                    fetch_reaponse: crawl.Result = crawl.fetch(
                        trying_url_list[j], self.word)
                    if domain in fetch_reaponse.domain_list:
                        identical_domain_list.append(domain)
                    if fetch_reaponse.is_include:
                        including_url_list.append(fetch_reaponse.self_url)
                    next_url_list += fetch_reaponse.href_list
                entire_url_list += trying_url_list
                trying_url_list.clear()
                trying_url_list += next_url_list
            return including_url_list
