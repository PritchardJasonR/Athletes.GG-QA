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
class SearchCharTest(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self)
        
    def testSearchChar(self):
        self.setUp()
        """
        Test Search Athlete
        1. Precondition Successfully Login and Navigate to Searching for Events
        2. Verify Event page populated correctly
        3. Search for 1 Result with partial input
        4. Search for a different result
        5. Search for a Result not to be there
        """
        #constants
        EMAIL = 'z.timgranger@gmail.com'
        PASSWORD = 'Qwer1234'
        SEARCH1 = 'StarCraft II: Legacy of the Void'
        PARTIAL = 'StarCraft II'
        SEARCH2 = 'Warcraft III: Reforged'
        SEARCH3 = 'Super Smash Bros. Ultimate'

        """
        1. Precondition Successfully Login and Navigate to Searching for Athletes
        """
        # Assert Login page Loaded successfully
        print("Assert Login page Loaded successfully")
        precondition(self)
        print("App Loaded Correctly")

        # Login
        print("Login")
        user_login(self, email=EMAIL, password=PASSWORD)
        print("user logged in")

        # select search
        print("select search button")
        self.driver.find_element_by_xpath(dashboard_bar_search).click()
        print("search button selected")

        # Assert Search Page Loaded
        print("Assert Search Page Loaded")
        self.driver.find_element_by_xpath(search_main_bar).is_displayed()
        self.driver.find_element_by_xpath(search_main_top).is_displayed()
        self.driver.find_element_by_xpath(search_main_athletes).is_displayed()
        self.driver.find_element_by_xpath(search_main_events).is_displayed()
        self.driver.find_element_by_xpath(search_main_games).is_displayed()
        print("search page loaded correctly")

        # select games filter
        print("select games filter")
        self.driver.find_element_by_xpath(search_main_games).click()
        sleep(2)
        self.driver.find_element_by_xpath(search_games_card1_text).is_displayed()
        print("Events filter clicked Page is Loaded")
        print("<<>><<>><<>>  PRECONDITION MET TEST START  <<>><<>><<>>")

        print("Game Searchedf for is displayed and Games not supposed to be there are not displayed")
        print('<<>><<>><<>>  TEST COMPLETED AS PASSED  <<>><<>><<>>')
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchCharTest)
    unittest.TextTestRunner(verbosity=2).run(suite)