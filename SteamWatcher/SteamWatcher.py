import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {
    'Accept': '',
    'Accept-Encoding': '',
    'Accept-Language': '',
    'Cache-Control': '',
    'Connection': '',
    'Cookie':'',
    'Host': '',
    'Sec-Fetch-Mode': '',
    'Sec-Fetch-Site': '',
    'Sec-Fetch-User': '',
    'Upgrade-Insecure-Requests': '',
    'User-Agent': ''
}

def parse_result_page(page_num):
    res = requests.get('https://store.steampowered.com/search/?category1=998?&page=%d'%page_num)
    soup = BeautifulSoup(res.text, 'html.parser')
    result_rows = soup.find_all('a', class_ = 'search_result_row')

    parse_result_rows(result_rows)


def parse_result_rows(result_rows):
    for result_row in result_rows:
        name = result_row.find('span', class_ = 'title').string.strip()

        if(result_row.find('div', class_ = 'search_price discounted') is not None):
            discounted_price = result_row.find('div', class_ = 'search_price discounted').text.strip()
            price = None
        else:    
            price = result_row.find('div', class_ = 'search_price').text.strip()
            discounted_price = None

        print("{}, {}, {}".format(name, price, discounted_price))


for i in range(5):
    parse_result_page(i)