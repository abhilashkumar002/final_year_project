'''
    Scrapping first 40 results of google search
'''

import requests
from bs4 import BeautifulSoup
import sys
import json

class GoogleScrapping:

    url = "http://www.google.com/search?num=50&q=news+"
    search_result_header = []
    search_result_link = []
    search_result_details = []

    def __init__(self):

        with open('query_upgrade.txt', 'r') as f:
            query = f.read()

        '''
        while True:
            query = input('Enter the topic to be searched...\n')
            if query is None:
                print('Query cannot be empty')
            else:
                break
        '''
        query = self.__format_query(query)
        self.url += query
        self.__scrap_query_result()

    def __format_query(self, query):
        query = str(query)
        query = query.replace(' ', '+')
        return query

    def __scrap_query_result(self):

        source_code = requests.get(self.url)
        soup = BeautifulSoup(source_code.text, 'lxml')

        # Soup headers
        for header_tag in soup.find_all('h3', attrs={'class':'r'}):
            if header_tag.find('a') and 'Images for ' not in header_tag.text and 'News for ' not in header_tag.text and 'Videos for ' not in header_tag.text:
                self.search_result_header.append(header_tag.text)

        # Soup links
        for cite_tag in soup.find_all('cite'):

            search_result = cite_tag.text.replace(' ', '')
            if '.' in search_result:
                if not str(search_result).startswith('http'):
                    search_result = 'http://' + search_result
                self.search_result_link.append(search_result)

        # Soup details
        for span_tag in soup.find_all('span', attrs={'class':'st'}):
            self.search_result_details.append(span_tag.text)

if __name__ == "__main__":

    googleScrapping = GoogleScrapping()

    #l = len(googleScrapping.search_result_link)
    l = 40
    '''
    for i in range(l):
        print(i)
        print('\n')
        print(googleScrapping.search_result_header[i])
        print('\n')
        print(googleScrapping.search_result_details[i])
        print('\n')
        print(googleScrapping.search_result_link[i])
        print('\n')
    '''
    dic = {}
    for i in range(l):
        dic[i] = {"header": googleScrapping.search_result_header[i]
        ,   "detail": googleScrapping.search_result_details[i]
        ,   "link": googleScrapping.search_result_link[i]
            }
    for i in range(0,len(dic)):
        print(dic[i])
        print("\n")
    # Storing the info into json style in .txt file
    write_file = open("resultDic" + ".json", "w", encoding="utf-8")
    json.dump(dic, write_file, ensure_ascii=False)
    write_file.close()