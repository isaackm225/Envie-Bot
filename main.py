from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

import os
import time



class Bot():
    def __init__(self):
        self.UNAME = input("Email: ")
        self.PWORD = input("placeholder_p: ")
        
    def fetch_tp(self):
        options = webdriver.ChromeOptions()
        with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
            driver.get('https://manage.tenantpay.com/login')
            uname_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.txtEmail>input')))
            uname_field.send_keys(self.UNAME)
            time.sleep(5)
            pwd_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.txtPassword>input')))
            pwd_field.send_keys(self.PWORD)
            time.sleep(5)
            #input_field.send_keys(Keys.ENTER)


    #Waits
    def document_initialized(driver):
        """Waiting for the doc to be ready"""
        return driver.find_element()

'''
def login_wait(driver):
    """Waiting for the bot to be logged in"""
    
    collection_box = driver.find_element(By.CLASS_NAME, "ion-inherit-color")
    box_string = collection_box.text
    if "CA$0.00" not in box_string:
        return True
    return False

def toggle_menu(driver):
    pages = driver.find_element(By.ID, "ag-2009-of-page-number")
    return pages


#Common Code
options = Options()
driver = webdriver.Chrome()

#"""
driver.get("https://manage.tenantpay.com/login")
WebDriverWait(driver, timeout=10).until(document_initialized)

## login page
uname_field = driver.find_element(By.NAME, "ion-input-0")
uname_field.send_keys(UNAME)
pword_field = driver.find_element(By.NAME, "ion-input-1")
pword_field.send_keys(PWORD)
pword_field.send_keys(Keys.ENTER)
WebDriverWait(driver, timeout=10).until(login_wait)

## landing page
toogle_menu = driver.find_element(By.CSS_SELECTOR, "ion-list>ion-menu-toggle:nth-of-type(2)")
toogle_menu.click()
a = toogle_menu(driver)
print(a.text)
#WebDriverWait(driver, timeout=10).until()

#download_button = driver.find_element(By.CSS_SELECTOR, "ion-button.md.button.button-solid.ion-activatable")
#print(download_button)
#download_button.click()
'''
if __name__=="__main__":
    bot = Bot()
    bot.fetch_tp()
