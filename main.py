
#  Python imports
from time import sleep
import xlsxwriter 
import xlsxwriter 
import pandas as pd
import openpyxl as op
from numpy import nan
import openpyxl as op
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class octopart:
    filename = 'results.xlsx'
    browser = None

    def __init__(self):
        self.create_excel_file()

    def scrape(self, partnumber):
        self.browser = webdriver.Chrome('chromedriver.exe') 
        self.digikey_login()
        url = 'https://octopart.com/search?q=' + partnumber + '&currency=USD&specs=0'
        self.browser.get(url)
        bs = self.browser.find_elements_by_tag_name("button")  
        for b in bs: 
            if b.text == 'Show All': b.click()
        soup = BeautifulSoup(self.browser.page_source, features='lxml')
        table = soup.find('table')
        tbody = table.find('tbody')
        trs = tbody.find_all('tr')
        print('\n\n')
        for tr in trs:
            if str(tr.get_text()).__contains__('Digi-Key') :
                stock = tr.find('td', attrs={'class': 'jsx-3779711368'})
                moq = tr.find('td', attrs={'class': 'jsx-3318793868'})
                price = tr.find('td', attrs={'class': 'jsx-1795508439'})
                sku = tr.find('td', attrs={'class': 'jsx-2389699081 sku'})
                
                moq = moq.get_text()
                sku = sku.find('a').get_text()
                stock = str(stock.get_text()).replace(',','')
                try: price = float(price.get_text())
                except: price = 'None'
                desc = 'None'
                try:
                    a = tr.find('a', attrs={'class': 'jsx-2100737765 click-url'})
                    link = a['href']
                    # print(link)
                    self.browser.get(link)
                    desc = self.digikey(self.browser.page_source)
                except: pass
                
                print('Digi-Key:')
                print('\tpartID = ', partnumber)
                print('\tSupplier Code = ', sku)
                print('\tMOQ = ', moq)
                print('\tStock = ', int(stock))
                print('\tPrice = ', price)
                self.write_to_excel(partnumber, desc, 'Digi-Key', link, sku, stock, moq, price)
                
            # if str(tr.get_text()).__contains__('Mouser') :
                # td = tr.find('td', attrs={'class': 'jsx-3779711368'})
                # value = str(td.get_text()).replace(',','')
                # td2 = tr.find('td', attrs={'class': 'jsx-1795508439'})
                # try: price = float(td2.get_text())
                # except: price = 'None'       
                # print('Mouser:')
                # print('\tpartID = ', partnumber)
                # print('\tStock = ', int(value))
                # print('\tPrice = ', price)
                # self.write_to_excel(partnumber, 'Mouser', value, price)

            # if str(tr.get_text()).__contains__('Farnell') :
                # td = tr.find('td', attrs={'class': 'jsx-3779711368'})
                # value = str(td.get_text()).replace(',','')
                # td2 = tr.find('td', attrs={'class': 'jsx-1795508439'})
                # try: price = float(td2.get_text())
                # except: price = 'None'
                # print('Farnell:')
                # print('\tpartID = ', partnumber)
                # print('\tStock = ', int(value))
                # print('\tPrice = ', price)
                # self.write_to_excel(partnumber, 'Farnell', value, price)
    
        sleep(5)
        print('\n\n')
        self.browser.quit()

    def digikey_login(self):   
        self.browser = webdriver.Chrome('chromedriver.exe') 
        login_url = 'https://auth.digikey.com/as/authorization.oauth2?response_type=code&client_id=pa_wam&redirect_uri=https%3A%2F%2Fwww.digikey.com%2Fpa%2Foidc%2Fcb&state=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiMnMiLCJzdWZmaXgiOiJqMlF6T0guMTYxNjE1NjE1MCJ9..2GHWxHGWNbzHWGmhnZy-bg.mOYu2qAf3Dpw5XtEa9k-T9dAkymsZddvUugkoGWVZC_AtbxvCJcGU1p6T6nW9tDQPZ5EhrOs5T5EPtDLhcRepDN0G9_bVYIvlsQYzBsk9gc.GA5-rxU38vBdh4ZUJwVIww&nonce=OzIsYKw5g25-48HBJ9SdSDok-fYrnuGMm1-_hR03u7w&scope=openid%20address%20email%20phone%20profile&vnd_pi_requested_resource=https%3A%2F%2Fwww.digikey.com%2FMyDigiKey&vnd_pi_application_name=DigikeyProd-Mydigikey'

        self.browser.get(login_url)
        elementID = self.browser.find_element_by_id('username')
        elementID.send_keys("adnanshahz2015@gmail.com")
        elementID = self.browser.find_element_by_id('password')
        elementID.send_keys("zeshan2015")
        elementID.submit()

        self.browser.get('https://www.digikey.com/en/products/detail/ERJ-8ENF1001V/P1.00KFCT-ND/89591?utm_campaign=buynow&utm_medium=aggregator&curr=usd&utm_source=octopart')
        self.browser.quit()

    def farnell_login(self):   
        login_url = 'https://uk.farnell.com/webapp/wcs/stores/servlet/LogonForm?myAcctMain=1&catalogId=15001&storeId=10151&langId=44'
        self.browser = webdriver.Chrome('chromedriver.exe') 
        self.browser.get(login_url)
        username = self.browser.find_element_by_id("logonId")
        password = self.browser.find_element_by_id("logonPassword")
        username.send_keys("adnanxshah")
        password.send_keys("Zeshan2015-")
        login = self.browser.find_element_by_link_text('Log In')
        login.click()
        print(login)
        sleep(5)

    def digikey(self, source=None):
        browser = webdriver.Chrome('chromedriver.exe') 
        browser.get('https://octopart.com/click/track?country=PK&ct=offers&ppid=55423196&sid=459&sig=0c18431&vpid=188064011')
        source = browser.page_source

        soup = BeautifulSoup(source, features='lxml')
        tbody = soup.find('tbody', attrs={'class' : 'MuiTableBody-root'})
        tr = tbody.find_all('tr')[4]
        print('tr = ', tr)
        td = tr.find_all('td')[1]
        print('td == ', td)
        desc = td.find('div').get_text()
        return desc

    def create_excel_file(self):
        # creating the file for the first time 
        # if not os.path.exists(self.filename):
        workbook = xlsxwriter.Workbook(self.filename)
        worksheet = workbook.add_worksheet("data")
        workbook.close()
        wb = op.load_workbook(self.filename, False)
        ws = wb['data']
        ws.append(['Manufacturing Part Number', 'Description', 'Distributor', 'Web URL', 'Supplier Code', 'Stock', 'MOQ', 'Price'])
        wb.save(self.filename)
        wb.close()

    def write_to_excel(self, partnumber, desc, distributor, web_url, supplier_code, stock, moq, price):
        wb = op.load_workbook(self.filename, False)
        ws = wb['data']
        ws.append([partnumber, desc, distributor, web_url, supplier_code, stock, moq, price])
        wb.save(self.filename)
        wb.close()


def selected_countries():
    part_list = []
    file_data =  pd.read_excel('data.xlsx', 'data')
    datas = file_data['manufacture part number']
    for i in datas.index:
        part_list.append(datas[i])
    return part_list

if __name__ == '__main__':
    obj = octopart()
    obj.digikey_login()
    # part_list = selected_countries() 
    # print(part_list)   
    # for part in part_list:
    #     obj.scrape(part)
    #     sleep(5)
    #     break


"""

We need the program to see the batch quantity needed and 
whether farnell, digikey, arrow or mouser have the stock available needed for the batch. 
if YES then it needs to pick the lowest price. 
if NO stock it would need to tell us that there was no stock available

"""
