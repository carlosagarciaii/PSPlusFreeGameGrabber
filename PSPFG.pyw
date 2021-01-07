from selenium import webdriver
import time
from random import randint
from _CoreTools import *

#PS Plus Free Games Module
class PSPFG:

    
    def rsleep(min = 3, max = 7):
        time.sleep(randint(min,max))

    def Go(driver):
            
        #Subscriptions
        driver.find_element_by_xpath('//a[contains(text(),"Subscriptions")]').click()

        #Free Games
        elements = driver.find_elements_by_xpath('//a//span[contains(text(),"Included")]/parent::*/strike')

        while (len(elements) == 0):
            elements = driver.find_elements_by_xpath('//a//span[contains(text(),"Included")]/parent::*/strike')
            PSPFG.rsleep(5,10)
            print('Current Element Count:' + str(len(elements)))

        driver.execute_script("arguments[0].scrollIntoView();",elements[0])
        PSPFG.rsleep()
        driver.execute_script("window.scrollBy(0,-120)")
        PSPFG.rsleep()

        
        while (len(driver.find_elements_by_xpath('//a//span[contains(text(),"Included")]/parent::*/strike')) > 0):
            element = driver.find_element_by_xpath('//a//span[contains(text(),"Included")]/parent::*/strike')
            driver.execute_script("arguments[0].scrollIntoView();",element)
            PSPFG.rsleep()
            driver.execute_script("window.scrollBy(0,-120)")
            PSPFG.rsleep()

            element.click()
            #Add to Library Button
            PSPFG.rsleep(7,14)
            element = driver.find_element_by_xpath('//button//*[contains(text(),"Add to Library")]/ancestor::button')
            driver.execute_script("arguments[0].scrollIntoView();",element)
            PSPFG.rsleep()
            driver.execute_script("window.scrollBy(0,-120)")
            PSPFG.rsleep()
            element.click()
            PSPFG.rsleep(min=2)
            driver.back()
            PSPFG.rsleep(min=2)
                       

