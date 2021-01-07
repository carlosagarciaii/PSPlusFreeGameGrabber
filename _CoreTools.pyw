from selenium import webdriver
from random import *
import time


class ct:
    def __init__(self,driver):
        self.driver = driver
        print('Driver set for gtools')
        

    def exceptionText(functionName,e):
        return '\n---------------------------\nEXCEPTION\n---------------------------\nFile:\t_CoreTools\nFunction:\t' + functionName + '\n' + e

    '''
    
        except Exception as e:
            raise ValueError(BingRewards.exceptionText('BingSearcher.Start',e))
            return False
        return True
    '''


    def NameV(self,name):
        driver = self.driver
        print('Attempting to locate element by name:\n\t\t' + name)
        try:
            element = driver.find_element_by_name(name)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nCould Not Find Name:\t' + name + '\n\n' + str(e) + '\n\n')
            return False
                
        return True

    def XpathV(self,xpath):
        driver = self.driver
        print('Attempting to locate Xpath:\n\t\t' + xpath)
        try:
            element = driver.find_element_by_xpath(xpath)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            
        except Exception as e:
            print('\n\nCould Not Find Xpath:\t' + xpath + '\n\n' + str(e) + '\n\n')
            return False
                
        return True

    def SafeClick(self,xpath):
        driver = self.driver
        print('SafeClicking on Xpath:\n\t\t' + xpath)
        try:
            element = driver.find_element_by_xpath(xpath)
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            element.click()
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nSafeClick Failed for Xpath:\t' + xpath + '\n\n' + str(e) + '\n\n')
            return False
        
        return True

    def SafeClickL(self,element):
        driver = self.driver
        print('SafeClickL on Element:\n\t\t' + str(element))
        try:
            driver.execute_script("arguments[0].scrollIntoView();",element)
            time.sleep(randint(3,5))
            element.click()
            time.sleep(randint(3,5))
        except Exception as e:
            print('\n\nSafeClickL failed for Element:\t' + str(element) + '\n\n' + str(e) + '\n\n')
            return False
        
        return True

    def HasText(self,xpath,text):
        driver = self.driver

        if ct(driver).XpathV(xpath):
            
            if text.lower() in driver.find_element_by_xpath(xpath).text.lower():
                return True
            else:
                return False
        else:
            return False

    def EWithText(self,xpath,text):
        driver = self.driver

        try:
            element = driver.find_element_by_xpath('//*[contains(translate(text(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"' + text.lower() + '")]')
            return element
        
        except Exception as e:
            print('\n\nEWithText feild to find Element\n\t' + str(element) + '\n\n' + str(e) + '\n\n')
            return False
        
        '''
        #elements = driver.find_elements_by_xpath(xpath + '[contains(text(),"' + text + '")]')
        elements = driver.find_elements_by_xpath(xpath)


        print('# of Elements ' + str(len(elements)))
        
        if len(elements) < 1:
            return False
        else:
            for element in elements:
                
                if text.lower() in element.text.lower():
                    return element
                    break
        ''' 


    def CloseOtherTabs(self):
        driver = self.driver
        try:
            while 1==1:
                driver.switch_to.window(self.driver.window_handles[1])
                driver.close()
        
        except Exception as e:
            print('\n\nException:\n' + str(e) + '\n\n')
            driver.switch_to.window(self.driver.window_handles[0])

class rsleep:
    def set(min = 3,max = 7):
        time.sleep(randint(min,max))
    def long():
        time.sleep(randint(6,20))
    def short():
        time.sleep(randint(1,3))
    


print('\n-------------------------------------\n_CoreTools Loaded\tSUCCESS\n-------------------------------------\n')






