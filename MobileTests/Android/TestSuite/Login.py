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
        Follow the Test Login Case
        Approach
        1. Assert login page selectors and text 
        2. Porper error messaging and invalid inputs at login
        3. login with valid credentials and assert user is logged into correct account
        """
        print("Driver created!")
        print("TEST STARTED!")

        # Constants
        EMAIL = 'z.timgranger@gmail.com'
        INVALEMAIL = 'ztim#gmail.co'
        PASSWORD = 'Qwer1234'
        INVALPASS = 'rewq4321'
        
        #Assert Login page loaded
        print("Assert Login page loaded")
        self.driver.implicitly_wait(20)
        sleep(2)
        self.driver.find_element_by_xpath(home_login_button).is_displayed()
        print("Login button visible")

        #click Button and assert user is at login page
        print("Click Login Button and assert user is at login page")
        self.driver.find_element_by_xpath(home_login_button).click()
        self.assertTrue(visible_xpath_assert(self, element= login_page_title))
        print("User has navigated to Login Page")

        # Assert Login Page Layout
        print("Assert Login Page Layout")
        self.driver.find_element_by_xpath(login_page_title).is_displayed()
        self.assertTrue(visible_xpath_assert(self, element=login_page_email_icon))
        self.assertTrue(visible_xpath_assert(self, element=login_page_email_field))
        self.assertTrue(visible_xpath_assert(self, element=login_page_password_icon))
        self.assertTrue(visible_xpath_assert(self, element=login_page_password_field))
        self.assertTrue(visible_xpath_assert(self, element=login_page_login_button))
        self.assertTrue(visible_xpath_assert(self, element=login_page_forgot_password_button))
        self.assertTrue(visible_xpath_assert(self, element=login_page_facebook))
        self.assertTrue(visible_xpath_assert(self, element=login_page_discord))
        self.assertTrue(visible_xpath_assert(self, element=login_page_twitch))
        self.assertTrue(visible_xpath_assert(self, element=login_page_twitter))
        self.assertTrue(visible_xpath_assert(self, element=login_page_youtube))
        
        logbutton_text = self.driver.find_element_by_xpath(login_page_login_button).text
        forgotbutton_text = self.driver.find_element_by_xpath(login_page_forgot_password_button).text
        facebook_text = self.driver.find_element_by_xpath(login_page_facebook).text
        discord_text = self.driver.find_element_by_xpath(login_page_discord).text
        twitch_text = self.driver.find_element_by_xpath(login_page_twitch).text
        twitter_text = self.driver.find_element_by_xpath(login_page_twitter).text
        youtube_text = self.driver.find_element_by_xpath(login_page_youtube).text

        self.assertEquals(logbutton_text, "LOG IN")
        self.assertEquals(forgotbutton_text, "Forgot Password")
        self.assertEquals(facebook_text,"Log In with Facebook")
        self.assertEquals(discord_text,"Log In with Discord")
        self.assertEquals(twitch_text,"Log In with Twitch")
        self.assertEquals(twitter_text,"Log In with Twitter")
        self.assertEquals(youtube_text,"Log In with YouTube")
        print(">> Login Page Layout Test Completed As Passed")
        
        # Invalid Login Test
        
        # Attempt to login with no credentials
        print("Attempt to login with no credentials")
        login_error_check(self, "Invalid login")
        print("Appropriate errormessage is displayed")
        
        # Valid email with no password
        print("Fill email with Valid select login and assert invalid toast appears")
        self.driver.find_element_by_xpath(login_page_email_field).send_keys(EMAIL)
        login_error_check(self, "Invalid login")
        
        print("Appropriate errormessage is displayed")

        # Valid email with invalid password
        print("Valid email with invalid password")
        self.driver.find_element_by_xpath(login_page_password_field).send_keys(INVALPASS)
        login_error_check(self, "Invalid login")
        print("Appropriate errormessage is displayed")

        # Invalid email with Valid Password
        print("Invalid email with Valid Password")
        self.driver.find_element_by_xpath(login_page_email_field).clear()
        self.driver.find_element_by_xpath(login_page_email_field).send_keys(INVALEMAIL)
        self.driver.find_element_by_xpath(login_page_password_field).clear()
        self.driver.find_element_by_xpath(login_page_password_field).send_keys(PASSWORD)
        login_error_check(self, "Invalid login")
        print("Appropriate errormessage is displayed")

        # Valid Credentials
        print("Valid Credentials")
        self.driver.find_element_by_xpath(login_page_email_field).clear()
        self.driver.find_element_by_xpath(login_page_password_field).clear()
        self.driver.find_element_by_xpath(login_page_email_field).send_keys(EMAIL)
        self.driver.find_element_by_xpath(login_page_password_field).send_keys(PASSWORD)
        self.driver.find_element_by_xpath(login_page_login_button).click()
        print("user is now logged in.  Error messaging test case completed as passed")

        # Assert user has navigated to dashboard and is logged in to the correct account
        print("Assert user has navigated to dashboard")
        self.driver.find_element_by_xpath(dashboard_title).is_displayed()
        print("User has navigated to dashboard")

        # Select profile and Assert user is logged into correct account
        print("Select profile and Assert user is logged into correct account")
        self.driver.find_element_by_xpath(dashboard_bar_profile).click()
        click_text(self, text= "Edit Profile")
        title = self.driver.find_element_by_xpath(edit_profile_title).text
        self.assertTrue(title, 'Profile')
        email_text = self.driver.find_element_by_xpath(edit_profile_email_text).text
        self.assertTrue(email_text, EMAIL)
        print("On Profile Page, Email is correct")

        # Log out
        print("Log Out")
        self.driver.find_element_by_xpath(edit_profile_menu).click()
        self.driver.find_element_by_xpath(menu_home).is_displayed()
        self.driver.find_element_by_xpath(menu_logout).click()
        self.driver.find_element_by_xpath(home_login_button).is_displayed()
        print("User is now logged out Test Completed as passed")
        print('*** Test is Complete *** ')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)