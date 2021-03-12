
#  Python imports
import threading
import json, time
import xlsxwriter 
import pandas as pd
from numpy import nan
import openpyxl as op
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class octopart:
    count = 0

    def scrape(self, partnumber):
        browser = webdriver.Chrome('chromedriver.exe') 
        url = 'https://octopart.com/search?q=' + partnumber + '&currency=USD&specs=0'
        browser.get(url)
        bs = browser.find_elements_by_tag_name("button")        
        for b in bs: 
            if b.text == 'Show All': b.click()
        soup = BeautifulSoup(browser.page_source, features='lxml')
        table = soup.find('table')
        tbody = table.find('tbody')
        trs = tbody.find_all('tr')
        for tr in trs:
            if str(tr.get_text()).__contains__('Digi-Key') :
                td = tr.find('td', attrs={'class': 'jsx-3779711368'})
                value = str(td.get_text()).replace(',','')
                td2 = tr.find('td', attrs={'class': 'jsx-1795508439'})
                try: price = float(td2.get_text())
                except: price = 'None'
                print('Digi-Key:')
                print('\tStock = ', int(value))
                print('\tPrice = ', int(price))
            if str(tr.get_text()).__contains__('Mouser') :
                td = tr.find('td', attrs={'class': 'jsx-3779711368'})
                value = str(td.get_text()).replace(',','')
                td2 = tr.find('td', attrs={'class': 'jsx-1795508439'})
                try: price = float(td2.get_text())
                except: price = 'None'
                print('Mouser:')
                print('\tStock = ', int(value))
                print('\tPrice = ', int(price))
            if str(tr.get_text()).__contains__('Farnell') :
                td = tr.find('td', attrs={'class': 'jsx-3779711368'})
                value = str(td.get_text()).replace(',','')
                td2 = tr.find('td', attrs={'class': 'jsx-1795508439'})
                try: price = float(td2.get_text())
                except: price = 'None'
                print('Farnell:')
                print('\tStock = ', int(value))
                print('\tPrice = ', int(price))
                # print('stock value = ', td.get_text())
                # try:
                #     a = tr.find('a', attrs={'class': 'jsx-2100737765 click-url'})
                #     link = a['href']
                #     print(link)
                #     browser.get(link)
                #     self.digikey(browser.page_source)
                #     time.sleep(5)
                # except: pass
                break
        time.sleep(5)
        browser.quit()


    def digikey(self, source):
        soup = BeautifulSoup(source, features='lxml')
        div = soup.find('div', attrs={'data-testid': 'qty-available-messages'})
        stockdiv = div.find_all('div')[0]
        stocks = str(stockdiv.get_text()).split(' ')
        stock_value = int(stocks[0])
        print('stock_value = ', stock_value)


def selected_countries():
    part_list = []
    file_data =  pd.read_excel('data.xlsx', 'data')
    datas = file_data['manufacture part number']
    for i in datas.index:
        part_list.append(datas[i])
    return part_list

if __name__ == '__main__':
    obj = octopart()
    part_list = selected_countries() 
    print(part_list)   
    for part in part_list:
        obj.scrape(part)
        break

"""

We need the program to see the batch quantity needed and 
whether farnell, digikey, arrow or mouser have the stock available needed for the batch. 
if YES then it needs to pick the lowest price. 
if NO stock it would need to tell us that there was no stock available

"""
