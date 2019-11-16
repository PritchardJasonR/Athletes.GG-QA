import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from DataUtils.PageObjects import *
from DataUtils.desired_capabilities import *
from Methods.custom_functions import *


# Returns abs path relative to this file instead of cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self)
        
    def testLogin(self):
        self.setUp()
        """
        Follow the Test Pad Account Creation Test Case
        @https://lncasoftware.ontestpad.com/script/1029
        """
        print("Driver created!")
        print("TEST STARTED!")

        EMAIL = 'Z.Tim.11GXXrasr@outlook.com'
        PASSWORD = '12345678Test'
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(login_button).is_displayed()
        self.driver.find_element_by_xpath(login_button).click()


        
        print('Test is Complete')

        # save the source to XML
        source = self.driver.page_source.encode('utf-8')
        with open("dashboard_source.xml", "wb") as file: 
            file.write(source)

    def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(create_account)
    unittest.TextTestRunner(verbosity=2).run(suite)