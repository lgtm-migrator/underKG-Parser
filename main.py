import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

import pandas as pd
import numpy as np

def BasicParse(URL, Target, DTail):
    List = []
    soup = BeautifulSoup(urlopen(URL), 'html.parser')

    if DTail == 'Text':
        for i in soup.select(Target):
            List.append(i.a.text)
    elif DTail == 'img':
        Temp = soup.find_all('div', {'class': 'thumb-wrap'})

        List = []
        for i in Temp:
            templ = i.img
            List.append(templ['src'])
    elif DTail == 'td':
        for i in soup.select(Target):
            List.append(i.text)
    elif DTail == 'All':
        for i in soup.select(Target):
            List.append(i)

    return List


class underkgParse:
    def __init__(self, num):
        self.num = str(num)

        self.url = 'http://underkg.co.kr/index.php?mid='

        self.news = f'news&page={num}'
        self.freeboard = f'freeboard&page={num}'
        self.qa = f'QnA&page={num}'

    def News(self):
        URL = self.url + self.news

        Title = BasicParse(
            URL, 'h1', 'Text')
        # List2 = BasicParse(URL, 'span.readNum')

        imageURL = BasicParse(
            URL, 'thumb-wrap', 'img')
        # imageURL = BasicParse(URL, 'img', 'img')

        return Title, imageURL

    def Freeboard(self):
        URL = self.url + self.freeboard

        Title = BasicParse(
            URL, "td.title", 'Text')[3:]
        Author = BasicParse(
            URL, "td.author", 'Text')[3:]
        readNum = BasicParse(
            URL, "td.readNum", 'td')[3:]
        FreeboardNo = BasicParse(
            URL, "td.no", 'td')

        return Title, Author, readNum, FreeboardNo

    def QnA(self):
        URL = self.url + self.qa

        Title = BasicParse(
            URL, 'td.title', 'Text')[3:]
        Author = BasicParse(
            URL, "td.author", 'Text')[3:]
        qaNo = BasicParse(
            URL, "td.no", 'td')
        return Title, Author, qaNo

if __name__ == "__main__":
    NewsTitle, imageURL = underkgParse(num=1).News()
    # FreeboardTitle, FreeboardAuthor, FreeboardReadNum, FreeboardNo = underkgParse(num=1).Freeboard()

    # qaTitle, qaAuthor, qaNo = underkgParse().QnA()

    # for i in imageURL:
    #     print(i)

    # print(pd.DataFrame([np.asarray(FreeboardTitle), np.asarray(FreeboardAuthor), np.asarray(FreeboardReadNum), np.asarray(FreeboardNo)]).T)
    print(pd.DataFrame([np.asarray(NewsTitle)]).T)

    # News = []
    # Freeboard = []
    # QnA = []

    # for i in range(1, 5):
    #     News.append(underkgParse(num=i).News())
    #     Freeboard.append(underkgParse(num=i).Freeboard())
    #     QnA.append(underkgParse(num=i).QnA())

    # News = np.asarray(News)
    # Freeboard = np.asarray(Freeboard)
    # QnA = np.asarray(QnA)

    # print(pd.DataFrame(News))
    # print(pd.DataFrame(Freeboard))
    # print(pd.DataFrame(QnA))

    # print(qaTitle[19], qaAuthor[19], qaNo[19])
    # print(imageURL[0])
