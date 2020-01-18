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

class SearchAthleteTest(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self)
        
    def testSearchAthlete(self):
        self.setUp()
        """
        Test Search Athlete
        1. Precondition Successfully Login and Navigate to Searching for Athletes
        2. Search for 1 Result
        3. Search for a Result not to be there
        4. Search for Results without ZeRo
        """
        #constants
        EMAIL = 'z.timgranger@gmail.com'
        PASSWORD = 'Qwer1234'
        SEARCH1 = 'ZeRo'
        SEARCH2 = 'ALANFORD'
        SEARCH3 = 'Liquid'

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

        # select athletes filter
        print("select athletes filter")
        self.driver.find_element_by_xpath(search_main_athletes).click()
        sleep(2)
        self.driver.find_element_by_xpath(search_athletes_card1_text).is_displayed()
        print("Athletes filter clicked")
        print("<<>><<>><<>>  PRECONDITION MET TEST START  <<>><<>><<>>")
        """
        2. Search for 1 Result
            # search for zero in card placeholder 1
        """
        # search for zero in card placeholder 1
        print("search for zero")
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH1)
        sleep(10)
        search_1_text = self.driver.find_element_by_xpath(search_athletes_card1_text).text
        self.assertTrue(search_1_text,SEARCH1)
        print("ZeRo found in placeholder 1")

        """
        3. Search for 0 Results to be there
        # search for ALANFORD
        # assert no cards are displayed
        """
        # 
        print("search for ALANFORD and no results are displayed")
        self.driver.find_element_by_xpath(search_main_bar).clear()
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH2)
        sleep(10)
        self.assertFalse(visible_xpath_assert(self, element= search_athletes_card2_text))
        print("no results are displayed")
        
        """
        4. Search for Results without ZeRo
        # search for Liquid
        # assert Cards are displayed
        # assert ZeRo is not displayed
        """
        # 
        print("search for Liquid and results are displayed")
        self.driver.find_element_by_xpath(search_main_bar).clear()
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH3)
        sleep(10)
        self.driver.find_element_by_xpath(search_athletes_card1_text).is_displayed()
        self.driver.find_element_by_xpath(search_athletes_card2_text).is_displayed()
        self.driver.find_element_by_xpath(search_athletes_card3_text).is_displayed()
        self.driver.find_element_by_xpath(search_athletes_card4_text).is_displayed()
        print("results are displayed")

        #Assert ZeRo is not in result
        print('Assert Zero is not in result')
        all_cards = athlete_cards_text(self)
        print(all_cards)
        self.assertFalse(search_results(self, text= SEARCH1, results_in_list= all_cards))
        print("Zero is not displayed")
        print('<<>><<>><<>>  TEST COMPLETED AS PASSED  <<>><<>><<>>')
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchAthleteTest)
    unittest.TextTestRunner(verbosity=2).run(suite)