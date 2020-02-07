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
        Test Search Char
        1. Precondition Successfully Login and Navigate to Searching for Chars
        2. Verify char page populated correctly
        3. Search for 1 Result with partial input
        4. Search for a different result
        5. Search for a Result not to be there
        """
        #constants
        EMAIL = 'z.timgranger@gmail.com'
        PASSWORD = 'Qwer1234'
        SEARCH1 = 'Zero Suit Samus'
        PARTIAL = 'Zero'
        SEARCH2 = 'Bowser'
        SEARCH3 = 'King'

        """
        1. Precondition Successfully Login and Navigate to Searching for Chars
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

        # select games filter then Char
        print("select games filter")
        self.driver.find_element_by_xpath(search_main_games).click()
        sleep(2)
        self.driver.find_element_by_xpath(search_games_card1_text).is_displayed()
        self.driver.find_element_by_xpath(search_main_chars).click()
        self.driver.find_element_by_xpath(search_chars_card1_text).is_displayed()
        print("Chars filter clicked Page is Loaded")
        print("<<>><<>><<>>  PRECONDITION MET TEST START  <<>><<>><<>>")
        """
        2. Verify char page populated correctly
        """
        self.driver.find_element_by_xpath(search_chars_card1_text).is_displayed()
        self.driver.find_element_by_xpath(search_chars_card1_game).is_displayed()
        self.driver.find_element_by_xpath(search_chars_card1_points).is_displayed()
        self.driver.find_element_by_xpath(search_chars_card1_heart).is_displayed()
        self.driver.find_element_by_xpath(search_chars_card2_text).is_displayed()
        self.driver.find_element_by_xpath(search_chars_card3_text).is_displayed()
        """
        3. Search for 1 Result with partial input
        """
        """
        3. Search for 1 Result with partial input
        """
        # search for Tech Republic V in card1 Text placeholder
        print(f"Search For {SEARCH1}using a Partial input")
        self.driver.find_element_by_xpath(search_main_bar).send_keys(PARTIAL)
        sleep(10)
        all_chars = athlete_cards_text(self)
        print(all_chars)
        self.assertTrue(search_results(self, text= SEARCH1, results_in_list= all_chars))
        print("First Search Was Successful")
        """
        4. Search for a different result
        """
        print('Searching something else')
        self.driver.find_element_by_xpath(search_main_bar).clear()
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH2)
        sleep(10)
        self.driver.swipe(start_x=30, start_y=400, end_x=30, end_y=900, duration=800)
        sleep(10)
        self.driver.find_element_by_xpath(search_chars_card1_text).is_displayed()
        all_cards = athlete_cards_text(self)
        print(all_cards)
        self.assertTrue(search_results(self, text= SEARCH2, results_in_list= all_cards))
        """
        5. Search for a Result not to be there
        """
        print(f"search for {SEARCH3} and results are displayed")
        self.driver.find_element_by_xpath(search_main_bar).clear()
        self.driver.find_element_by_xpath(search_main_bar).send_keys(SEARCH3)
        sleep(10)
        self.driver.swipe(start_x=30, start_y=400, end_x=30, end_y=900, duration=800)
        sleep(10)
        # assert Sammus and Bowser are not displayed
        print(f'Assert {SEARCH1} and {SEARCH2} are Not displayed and King is')
        all_cards1 = games_cards_text(self)
        print(all_cards1)
        self.assertTrue(search_results(self, text= SEARCH3, results_in_list= all_cards1))
        self.assertFalse(search_results(self, text= SEARCH1, results_in_list= all_cards1))
        self.assertFalse(search_results(self, text= SEARCH2, results_in_list= all_cards1))
        print("Char Searched for is displayed and Chars not supposed to be there are not displayed")
        print('<<>><<>><<>>  TEST COMPLETED AS PASSED  <<>><<>><<>>')
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchCharTest)
    unittest.TextTestRunner(verbosity=2).run(suite)