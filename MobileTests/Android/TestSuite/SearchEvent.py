#Riptide
#Tech Republic V
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
class SearchEventTest(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self)
        
    def testSearchEvent(self):
        self.setUp()
        """
        Test Search Athlete
        1. Precondition Successfully Login and Navigate to Searching for Events
        2. Search for 1 Result
        3. Verify Event page populated correctly
        4. Search for a different result
        5. Search for a Result not to be there
        """
        #constants
        EMAIL = 'z.timgranger@gmail.com'
        PASSWORD = 'Qwer1234'
        SEARCH1 = 'Tech Republic V'
        SEARCH2 = 'Riptide'
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
        self.driver.find_element_by_xpath(search_main_events).click()
        sleep(2)
        self.driver.find_element_by_xpath(search_events_card1_text).is_displayed()
        print("Events filter clicked Page is Loaded")
        print("<<>><<>><<>>  PRECONDITION MET TEST START  <<>><<>><<>>")
        """
        2. Search for 1 Result
        """
        # search for Tech Republic V in card1 Text placeholder
        print("search for Tech Republic V")
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH1)
        sleep(10)
        search_1_text = self.driver.find_element_by_xpath(search_events_card1_text).text
        print(search_1_text)
        self.assertTrue(search_1_text,SEARCH1)
        print("Tech Republic V found in placeholder 1")
        """
         3. Verify Event page populated correctly
        """
        print("Verify Event page populated correctly")
        self.driver.find_element_by_xpath(search_events_card1_text).is_displayed()
        self.driver.find_element_by_xpath(search_events_card1_type).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_points).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_game).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_upcoming).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_notify).is_displayed()
        print('Search for events is populated as expected')
        """
        4. Search for a different result
        """
        print('Search for a different result')
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH2)
        sleep(10)
        self.driver.swipe(start_x=30, start_y=400, end_x=30, end_y=900, duration=800)
        sleep(10)
        search_2_text = self.driver.find_element_by_xpath(search_events_card1_text).text
        print(search_2_text)
        self.assertTrue(search_2_text,SEARCH2)
        """
        5. Search for a Result not to be there
        # search for Liquid
        # assert Cards are displayed
        # assert Tech Republic V is not displayed
        """
        print("search for Liquid and results are displayed")
        self.driver.find_element_by_xpath(search_main_bar).clear()
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH3)
        sleep(10)
        self.driver.swipe(start_x=30, start_y=400, end_x=30, end_y=900, duration=800)
        sleep(10)
        # Verify Event page populated correctly
        print("Verify Event page populated correctly")
        self.driver.find_element_by_xpath(search_events_card1_text).is_displayed()
        self.driver.find_element_by_xpath(search_events_card1_type).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_points).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_game).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_upcoming).is_displayed()
        self.driver.find_element_by_xpath(search_events_card_notify).is_displayed()
        print('Search for events is populated as expected')

        # assert Tech Republic V is not displayed
        print('Assert Tech Republic V and Riptide are not in result')
        all_cards = events_cards_text(self)
        print(all_cards)
        self.assertFalse(search_results(self, text= SEARCH1, results_in_list= all_cards))
        self.assertFalse(search_results(self, text= SEARCH2, results_in_list= all_cards))
        print("Event is not displayed")
        print('<<>><<>><<>>  TEST COMPLETED AS PASSED  <<>><<>><<>>')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchEventTest)
    unittest.TextTestRunner(verbosity=2).run(suite)