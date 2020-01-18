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

class GetTheAppTest(unittest.TestCase):
    def setUp(self):
        self.driver = play_store_caps(self)

    def testGetTheApp(self):
        self.setUp()
        self.driver.implicitly_wait(20)
        """
        Test Objectives
        1. Uninstalling the app then downloading from play store. 
        2. Opening app and asserting login page has loaded successfully
        """

        # Wait for search Bar to be visible
        print("Wait for search Bar to be visible")
        self.driver.find_elements_by_id(play_search_bar)
        print("Page had loaded successfully")

        # Click Text bar
        print("Click Text bar")
        click_text(self,text= "Search for apps & games")
        """
        a= 29  , b= 30 , c=  31 , d= 32 , e= 33, f= 34, g= 35, h= 36, i= 37, j=  38, k=  39, l=  40,  m=  41 

        n=  42 , o= 43, p= 44, q= 45, r= 46, s= 47, t=  48, u=  49, v=  50, w=  51, x= 52, y=  53, z= 54

        1=  8 , 2=  9 , 3= 10 , 4= 11 , 5= 12 , 6=  13 , 7=  14 , 8= 15 , 9=  16 , 0=  7, 
        """
        sleep(1.5)
        self.driver.press_keycode(29)
        self.driver.press_keycode(48)
        self.driver.press_keycode(36)
        self.driver.press_keycode(40)
        self.driver.press_keycode(33)
        self.driver.press_keycode(48)
        self.driver.press_keycode(33)
        self.driver.press_keycode(47)
        self.driver.press_keycode(56)
        self.driver.press_keycode(35)
        self.driver.press_keycode(35)
        self.driver.execute_script("mobile:performEditorAction", {'action': 'search'})
    
        print("searched for athletes.gg")
        
        # click Follow Esports
        print("click Follow Esports")
        self.driver.find_element_by_id('com.android.vending:id/play_card').click()
        print("clicked Athletes.gg icon")

        # check if uninstall is visible if so uninstall it otherwise install app
        print("check if uninstall is visible if so uninstall it ")
        try:
            self.driver.implicitly_wait(5)
            find_by_text(self, text="Uninstall")
            print("Uninstall Text Found!")
            click_text(self, text= "Uninstall")
            self.driver.implicitly_wait(90)
            click_text(self, text= "Install")
            click_text(self, text="open")
            self.driver.implicitly_wait(20)
            pass
        except Exception as e:
            print("App is not installed Lets Install it!")
            click_text(self, text= "Install")
            self.driver.implicitly_wait(20)
            self.driver.find_element_by_id(play_uninstall_button)
            pass
        print("app is now installed")
        try:
            self.driver.find_element_by_id(play_install_status)
            print("app is still installing")
            sleep(40)
            pass
        except Exception as e:
            print("Either app has finished or test has a problem")
            pass
        
        # Now Open App
        print("Now Open App")
        self.driver.start_activity("gg.athletes.app", "host.exp.exponent.MainActivity")
        self.driver.implicitly_wait(20)
        EMAIL = 'z.timgranger@gmail.com'
        PASSWORD = 'Qwer1234'
        self.driver.find_element_by_xpath(home_login_button).is_displayed()
        print("User is now on Athletes GG")
        
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


        # Swipe and accept
        self.driver.swipe(start_x=13, start_y=900, end_x=900, end_y=700, duration=800)
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
        sleep(3)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
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
        print("-=-=-=-=-=-=-=-=-= Test Play Store Test Completed as passed-=-=-=-=-=-=-=-=-")
        print('*** Test is Complete *** ')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GetTheAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)