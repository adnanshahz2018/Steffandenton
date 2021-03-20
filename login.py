#  Python imports
from time import sleep
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display


# selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

class Request:
    # logger = logging.getlogger('django.project.request')
    selenium_retries = 0
    browser = None
    url = None

    def __init__(self, url):
        self.url = url

    def get_selenium_res(self, class_name=None):
        try:
            software_names = [SoftwareName.CHROME.value]
            operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
            user_agent = user_agent_rotator.get_random_user_agent()

            chrome_options = Options()
            # # chrome_options.add_argument('--headless')            
            # # chrome_options.add_argument('--no-sandbox')            
            chrome_options.add_argument('--window-size=860,1080')            
            # chrome_options.add_argument('--disable-gpu')            
            # chrome_options.add_argument(f'user-agent={user_agent}')
            chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.delete_all_cookies()
            driver.set_window_position(500,0)
            self.browser = driver

            # -----------------------------------------------------------
                            # Due Task: PROXY SECTION
            # -----------------------------------------------------------

            self.browser.get(self.url)
            elementID = self.browser.find_element_by_id('username')
            elementID.send_keys("adnanshahz2015@gmail.com")
            elementID = self.browser.find_element_by_id('password')
            elementID.send_keys("zeshan2015")
            elementID.submit()

            sleep(5)
            self.browser.quit()
        except: pass

class login:
    browser = None

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


if __name__ == '__main__':
    login_url = 'https://auth.digikey.com/as/authorization.oauth2?response_type=code&client_id=pa_wam&redirect_uri=https%3A%2F%2Fwww.digikey.com%2Fpa%2Foidc%2Fcb&state=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiMnMiLCJzdWZmaXgiOiJqMlF6T0guMTYxNjE1NjE1MCJ9..2GHWxHGWNbzHWGmhnZy-bg.mOYu2qAf3Dpw5XtEa9k-T9dAkymsZddvUugkoGWVZC_AtbxvCJcGU1p6T6nW9tDQPZ5EhrOs5T5EPtDLhcRepDN0G9_bVYIvlsQYzBsk9gc.GA5-rxU38vBdh4ZUJwVIww&nonce=OzIsYKw5g25-48HBJ9SdSDok-fYrnuGMm1-_hR03u7w&scope=openid%20address%20email%20phone%20profile&vnd_pi_requested_resource=https%3A%2F%2Fwww.digikey.com%2FMyDigiKey&vnd_pi_application_name=DigikeyProd-Mydigikey'
    req = Request(login_url)
    req.get_selenium_res()


"""
cdc_asdjflasutopfhvcZLmcfl_
newjerseycourlinerfantastic

btlhsaxJbTXmBATUDvTRhvcZLm_
newjerseycourlinerfantastic
"""