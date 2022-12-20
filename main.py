import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# if Firefox:
"""
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #this module makes sure the gecko driver is added to the path before execution
#"""

#if Edge:
#"""
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#"""

#CREDENTIALS AND CONSTANTS
UNAME = input("Email: ")
PWORD = input("placeholder_p: ")

#Waits
def document_initialized(driver):
    """Waiting for the doc to be ready"""
    return driver.execute_script("return document.readyState")

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
options.add_experimental_option("detach", True)
#if Edge:
# """
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
#"""
#if Firefox:
"""
binary = FirefoxBinary('C:\Firefox\Firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
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