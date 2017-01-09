# !/usr/bin/venv python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import xlsxwriter
import urllib.parse
from io import BytesIO
from urllib.request import urlopen
import threading
import os
from queue import Queue

class MyWorkbook(object):
    def __init__(self):
        self.__count = 0
        self.__workbook = xlsxwriter.Workbook('fang.xlsx')
        self.__worksheet = self.__workbook.add_worksheet("mySheet")
        self.__worksheet.set_column(0, 0, 20)
        self.__worksheet.set_column(1, 6, 40)
        self.__worksheet.set_default_row(40, True)

    def get_work_book(self):
        return self.__workbook

    def set_count(self, c):
        self.__count = c

    def download(self, url):
        print(url)
        response = requests.get(url)
        content = ""
        if response.status_code == 200:
            content = response.content

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        lis = soup.find_all('li', class_="clear")

        for li in lis:
            soup = BeautifulSoup(str(li), 'html.parser', from_encoding='utf-8')
            t1 = soup.find("div", class_="title").find("a").get_text()
            t2 = soup.find("div", class_="address").get_text()
            t3 = soup.find("div", class_="flood").find("div", class_="positionInfo").get_text()
            t4 = ""
            t4Soup = soup.find("div", class_="tag").find("span", class_="taxfree")
            if t4Soup is not None:
                t4 = t4Soup.get_text()
            print(t4)
            t5 = soup.find("div", class_="priceInfo").find("div", class_="unitPrice").find("span").get_text()
            t6 = soup.find("img", class_="lj-lazy")['data-original']
            print(t6)
            if t6 is not None and t6 != "":
                image_data = BytesIO(urlopen(t6).read())
                self.__worksheet.insert_image(self.__count, 0, t6, {'image_data': image_data})
            self.__worksheet.write(self.__count, 1, t1)
            self.__worksheet.write(self.__count, 2, t5)
            self.__worksheet.write(self.__count, 3, t2)
            self.__worksheet.write(self.__count, 4, t3)
            self.__worksheet.write(self.__count, 5, t4)
            self.__count += 1
            print(self.__count)


if __name__ == "__main__":
    w = MyWorkbook()
    for i in [x for x in range(1, 2)]:
        print(i)
        w.download("http://hz.lianjia.com/ershoufang/pg"+str(i))
    w.get_work_book().close()



