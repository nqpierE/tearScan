import requests
from requests import Response
from bs4 import BeautifulSoup, ResultSet


class Result:
    self_url: str
    is_include: bool
    href_list: list[str]
    domain_list: list[str]

    def __init__(self, self_url, is_include, href_list, domain_list):
        self.self_url = self_url
        self.is_include = is_include
        self.href_list = href_list
        self.domain_list = domain_list


def fetch(url: str, word: str):
    is_include: bool = False
    response: Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')
    atag_list: ResultSet = soup.find_all('a')
    if word in response.text:
        is_include = True
    href_list: list[str] = []
    domain_list: list[str] = []
    for atag in atag_list:
        try:
            href: str = str(atag["href"])
        except:
            break
        if "https://" in href or "http://" in href:
            href_list.append(href)
            domain_list.append(href.split("/")[2])
    result: Result = Result(url, is_include, href_list, domain_list)
    return result
