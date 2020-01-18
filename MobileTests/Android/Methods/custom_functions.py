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

user_email = "fmui_testing@legrand.us"
user_password = "Testing1"

def search_results(self, text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False

def athlete_cards_text(self):
    self.driver.implicitly_wait(10)
    card_list = []
    xpath = "//android.view.ViewGroup/android.view.ViewGroup["
    xpathend = "]/android.view.ViewGroup[2]/android.widget.TextView[1]"
    for index in range(1, 15):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def user_login(self, email, password):
    self.driver.find_element_by_xpath(login_page_email_field).clear()
    self.driver.find_element_by_xpath(login_page_email_field).send_keys(email)
    self.driver.find_element_by_xpath(login_page_password_field).clear()
    self.driver.find_element_by_xpath(login_page_password_field).send_keys(password)
    self.driver.find_element_by_xpath(login_page_login_button).click()

    # Assert user has navigated to dashboard and is logged in to the correct account
    self.driver.find_element_by_xpath(dashboard_title).is_displayed()
    print("User has navigated to dashboard")

def precondition(self):

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
        
def swipe(self):
    self.driver.swipe(start_x=13, start_y=900, end_x=900, end_y=700, duration=800)

def add_new_category(self, text):
    self.driver.find_element_by_xpath(s_add_new).is_displayed()
    self.driver.find_element_by_xpath(s_add_new).click()
    self.driver.find_element_by_xpath(s_name_entry).is_displayed()
    self.driver.find_element_by_xpath(s_name_entry).send_keys(text)
    self.driver.find_element_by_xpath(s_ok).click()
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_xpath(s_add_new).is_displayed()
    if find_by_text(text): 
        print(f'Category {text} successfully added')
    else: 
        raise AssertionError(f'Category {text} was not created')

def login_error_check(self, text):
    self.driver.find_element_by_xpath(login_page_login_button).click()
    self.driver.find_element_by_xpath(login_invalid_text).is_displayed()
    err = self.driver.find_element_by_xpath(login_invalid_text).text
    self.assertEquals(err, text ,"Wrong error message is displayed")
    self.driver.find_element_by_xpath(login_invalid_ok).click()    

def click_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).click()

def find_by_text(self, text):
    if  not self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).is_displayed():
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def search_bar(self, text):
    self.driver.find_element_by_id(d_search_bar).send_keys(text)
    self.driver.find_element_by_id(d_search_bar).click()
    self.driver.implicitly_wait(10)
    self.driver.execute_script("mobile:performEditorAction", {'action': 'go'})
    # self.driver.hide_keyboard()
    self.driver.implicitly_wait(10)

def loc_search_key(self):
    self.driver.implicitly_wait(10)
    key_list = []
    xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout['
    xpathend = ']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView'
    for index in range(2, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            key_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return key_list

def locations_cards(self):
    self.driver.implicitly_wait(10)
    play_list = []
    xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
    xpathend = "]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            play_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return play_list

def loc_search_cards(self):
    self.driver.implicitly_wait(10)
    play_list = []
    xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ListView/android.widget.LinearLayout['
    xpathend = ']/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView'
    for index in range(2, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            play_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return play_list

def site_cards(self):
    self.driver.implicitly_wait(10)
    card_list = []
    xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
    xpathend = "]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView"
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def item_groupings(self, item_type):
    item_type_list = []
    if item_type == "RC":
        item_type_list.append("")
    elif item_type == "SW":
        item_type_list.append('')
        item_type_list.append('')
    elif item_type == "OS":
        item_type_list.append("")
        item_type_list.append("")
    elif item_type == "DL":
        item_type_list.append("")
    elif item_type == "LO":
        print('Loads Dont Exist Yet ^.^')
        
    return item_type_list

def visible_xpath_assert(self, element):        
    self.driver.implicitly_wait(5)
    if not self.driver.find_elements(By.XPATH, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def visible_accessibility_id_assert(self, element):        
    self.driver.implicitly_wait(5)
    if not self.driver.find_elements(MobileBy.ACCESSIBILITY_ID, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def debug_xpath_assert(self, element):        
    self.driver.implicitly_wait(50000)
    if not self.driver.find_elements(By.XPATH, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def debug_accessibility_id_assert(self, element):        
    self.driver.implicitly_wait(50000)
    if not self.driver.find_elements(MobileBy.ACCESSIBILITY_ID, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def get_SMS_string(self):
    # Navigate to SMS application
    self.driver.implicitly_wait(20)
    activity = self.driver.current_activity
    self.driver.start_activity("com.adhoclabs.burner", ".BurnerMainDrawerActivity")
    print('Switching Application To Check SMS Message!')

    #Assert User Successfully Navigated to App HomePage 
    self.assertTrue(self.driver.find_element_by_id('com.adhoclabs.burner:id/main_content').is_displayed())

    # Identify New Message Notification and click
    new_msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status')
    self.assertTrue(new_msg.is_displayed())

    # Read Message
    msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status')

    # Grab the text from message
    msg_text = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status').text

    # seperate the message to get the Recovery code 
    recov_code = msg_text.split()[3]
    # print that the code was successfully identified 
    print(recov_code)

    # Long Press selector to delete message
    actions = TouchAction(self.driver)
    actions.long_press(msg)
    actions.perform()

    # Actually Delete message
    delte_msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/buttonDefaultPositive')
    self.assertTrue(delte_msg.is_displayed())
    delte_msg.click()

    # assert the message was successfully deleted
    self.assertTrue(EC.invisibility_of_element_located((By.ID, 'com.adhoclabs.burner:id/call_status')))
    print('Message Successfully Deleted!')

    print(f'Navigating back to Legrand app your Recoverycode is {recov_code}')
    self.driver.start_activity('', activity)

    return recov_code

def get_email_string(self):
    """
    @ Gets the randomized activity, and navigates to yahoo app
    @ Looks at e-mail gets the recoverycode and deletes the e-mail
    @ navigates back to legrand app with the recovery code
    """
    # Store App Activity and navigate to Yahoo app
    self.driver.implicitly_wait(60)
    activity = self.driver.current_activity
    self.driver.hide_keyboard()
    self.driver.implicitly_wait(10)
    self.driver.start_activity("com.yahoo.mobile.client.android.mail", "com.yahoo.mobile.client.android.mail.activity.MainActivity")
    print('Switching Application To Check Email Message and get the password recovery code!')
    
    #verify user has successfully navigated to yahoo application
    self.driver.hide_keyboard()
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_list').is_displayed())
    while not self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_unread_indicator').is_displayed():
        sleep(5)
        self.driver.swipe(start_x=750, start_y=1250, end_x=750, end_y=1750, duration=800)
    self.driver.implicitly_wait(60)


    # Verify New Email exists and Grab the text from message
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_unread_indicator').is_displayed())
    email_text = self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_text').text

    # seperate the message to get the Recovery code 
    recov_code = email_text.split()[3]
    # print that the code was successfully identified 
    print(recov_code)

    # Long Press selector to delete message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').click()

    # Delete Message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').click()

    # Assert eMail Was deleted
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/empty_view_text').is_displayed())

    # go back to legrand app
    print(f'Navigating back to Legrand app your Recoverycode is {recov_code}')
    self.driver.start_activity('', activity)

    return recov_code

def state_assertion(self): 
    #set up 
    states_list = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    state = self.driver.find_element_by_xpath(site_state_text).text
    print(state)
    # function
    if state in states_list:
        print('Matches state abbreviation')      
    else: 
        raise AssertionError('State abbreviation is incorrect')
