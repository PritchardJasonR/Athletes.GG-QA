import os
import unittest
import datetime
import time
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

class MetricsTest(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self)
        
    def testMetrics(self):
        self.setUp()
        """
        Test Search Athlete
        1. Precondition Successfully Login and Navigate to Searching for Athletes
        2. Layout
        3. Categories
        4. Search for Athlete
        5. Search for event
        6. Search for Game
        7. Search for Characters
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
        self.driver.implicitly_wait(10)
        user_login_time(self, email=EMAIL, password=PASSWORD)
        self.driver.find_element_by_xpath(login_page_login_button).click()
        startl = time.time()

        # Assert user has navigated to dashboard and is logged in to the correct account
        self.driver.find_element_by_xpath(dashboard_title).is_displayed()
        endl = time.time()
        print("User has navigated to dashboard")
        print("user logged in")

        # select search
        print("select search button")
        self.driver.find_element_by_xpath(dashboard_bar_search).click()

        # Time Top page to load
        startd = time.time()
        self.driver.find_element_by_xpath(search_top_card6_fav).is_displayed()
        endd = time.time()
        print("search button selected")

        # Assert Search Page Loaded
        print("Assert Search Page Loaded")
        self.driver.find_element_by_xpath(search_main_bar).is_displayed()
        self.driver.find_element_by_xpath(search_main_top).is_displayed()
        self.driver.find_element_by_xpath(search_main_athletes).is_displayed()
        self.driver.find_element_by_xpath(search_main_events).is_displayed()
        self.driver.find_element_by_xpath(search_main_games).is_displayed()
        print("search page loaded correctly")
        print('<><><><><><> PRECONDITION MET TEST START <><><><><><><><><>')
        """
        1. Layout
        # Nav Bar
        # Some Results Displayed
        """
        # Assert Nav bar is displayed as expected
        self.driver.find_element_by_xpath(dashboard_athletes_tab).is_displayed()
        self.driver.find_element_by_xpath(dashboard_events_tab).is_displayed()
        self.driver.find_element_by_xpath(dashboard_games_tab).is_displayed()

        # Assert Search page loads with athletes and events where they are supposed to be
        ath_txt = self.driver.find_element_by_xpath(search_top_athletes_div).text
        eve_txt = self.driver.find_element_by_xpath(search_top_events_div).text
        self.assertEqual(ath_txt, 'Athletes')
        self.assertEqual(eve_txt, 'Events')

        #Start Timer for logging Top Load Time

        login_time = int(endl - startl)
        diag_time = int(endd - startd)
        login_minutes = (login_time) // 60
        diag_minutes = (diag_time) // 60
        login_seconds = (login_time % 60)
        diag_seconds = (diag_time % 60)
        now = datetime.datetime.now()
        filename = f'Login_Search_Load_Times{now.strftime("%Y-%m-%d_%H-%M")}'
        with open(PATH(f"test_metrics/{filename}.txt"),'w') as result:
            result.write('[][][][][][][][][][ Time To Login / Diagnostics TEST RESULTS ][][][][][][][][][][]][][][][][]\n\n')
            result.write(f'Login {login_minutes} Minutes to run\n\n')
            result.write(f'Login {login_seconds} Seconds to run\n\n')
            result.write(f'Top Search Page took {diag_minutes} Minutes to Load\n\n')
            result.write(f'Top Search Page took {diag_seconds} Seconds to Load\n\n')
        self.driver.quit()
            
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MetricsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)