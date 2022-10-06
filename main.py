from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #this module makes sure the gecko driver is added to the path before execution
#binary = FirefoxBinary('C:\Firefox\Firefox.exe')
#driver = webdriver.Firefox(firefox_binary=binary)
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



"""
#extracting resident code

with open("Delinquency_Report_October_4_2022.csv", "r", newline="") as report:
    reader = csv.DictReader(report,dialect="excel", delimiter=",", quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row['Code'])
"""
"""

"""

driver = webdriver.Firefox()
driver.get("https://www.yardiaspcn6.com/08930ashcro/pages/menu.aspx?sMenuSet=StudentHousing")