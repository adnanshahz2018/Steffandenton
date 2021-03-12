
#  Python imports
import threading
import json, time
import xlsxwriter 
import pandas as pd
from numpy import nan
import openpyxl as op
from bs4 import BeautifulSoup
from selenium import webdriver 


class octopart:
    count = 0

    def scrape(self, partnumber):
        browser = webdriver.Chrome('chromedriver.exe') 
        browser.get(f'https://octopart.com/search?q={partnumber}&currency=USD&specs=0')
        source = browser.page_source

class digikey:
    pass

class farnell:
    pass



def selected_countries():
    part_list = []
    file_data =  pd.read_excel('data.xlsx', 'data')
    datas = file_data['manufacture part number']
    for i in datas.index:
        part_list.append(datas[i])
    return part_list

if __name__ == '__main__':
    part_list = selected_countries() 
    print(part_list)   



