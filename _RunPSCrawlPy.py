from selenium import webdriver
import os,sys,re,time,pyautogui
import pandas as pd
from datetime import datetime
from random import randint
from _CoreTools import *
from PSPFG import *

'''
book = openpyxl.load_workbook(targetXLS)
sheet = book.active
rowCount = sheet.max_row
'''

class PSCrawl:
    def __init__(self):
        pass

    def BrowserKicker(browser):
        if (browser.lower() == "chrome" or browser.lower() == "google"):
            driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        elif browser.lower() == "edge" :
            driver = webdriver.Edge(executable_path='../Drivers/msedgedriver.exe')
        elif (browser.lower() == "ie" or browser.lower() == "explorer" or browser.lower() == "iexplore"):
            driver = webdriver.Ie(executable_path='../Drivers/IE../Driverserver.exe')
        elif (browser.lower() == "firefox" or browser.lower() == "ff" or browser.lower() == "mozilla"):
            driver = webdriver.Firefox(executable_path='../Drivers/geckodriver.exe')
        return driver


driver = PSCrawl.BrowserKicker('ff')

driver.get('http://store.playstation.com')
rsleep.set()

driver.find_element_by_xpath('//button[@data-qa="web-toolbar#signin-button"]').click()
rsleep.set()

#UserName
driver.find_element_by_xpath('//input[@id="ember20"]').send_keys(sys.argv[1])
driver.find_element_by_xpath('//button/*[contains(text(),"Next")]').click()
rsleep.set()

#Password
driver.find_element_by_xpath('//input[@id="ember37"]').send_keys(sys.argv[2])
driver.find_element_by_xpath('//button/*[contains(text(),"Sign In")]').click()
rsleep.set(7,15)

#2Step
twoStepEnabled = driver.find_elements_by_xpath('//*[contains(text(),"2-step verification is enabled")]')
if (len(twoStepEnabled) > 0):
    messageAlert = 'You must complete 2 Step Verification before this script can run.'
    print(messageAlert)
    pyautogui.alert(text=messageAlert, title='2-Step Validation', button='OK')
    # button/[verify]

PSPFG.Go(driver)

rsleep.short()

driver.close()
