import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from datautils.page_objects import * 

user_email = "fmui_testing@legrand.us"
user_password = "Testing1"

def login_function(self):
     
    self.driver.find_element_by_accessibility_id('EmailEntry').is_displayed()
    self.driver.find_element_by_accessibility_id('EmailEntry').send_keys(user_email)
    self.driver.find_element_by_accessibility_id('PasswordEntry').send_keys(user_password)
    self.driver.find_element_by_xpath(l_btn).click()
    self.assertTrue(self.driver.find_element_by_accessibility_id(d_slct_facility).is_displayed())
    print('Logged in')
     

def select_account(self): 
    self.driver.swipe(start_x=13, start_y=900, end_x=900, end_y=700, duration=800)
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_xpath(m_settings_no_site).is_displayed()
    self.driver.find_element_by_xpath(m_settings_no_site).click()
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_xpath(m_account).is_displayed()
    self.driver.find_element_by_xpath(m_account).click()
    print('Account selected')

def swipe(self):
    self.driver.swipe(start_x=13, start_y=900, end_x=900, end_y=700, duration=800)

def swipe_close(self):
    self.driver.swipe(start_x=900, start_y=700, end_x=13, end_y=900, duration=800)

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
            


def user_login(self, email, password):
    self.driver.implicitly_wait(10)
    # Assert Home page is Loaded
    self.assertTrue(visible_xpath_assert(self, element= l_page_ident),'User is not on login page')
    
    # Selectors for custom function
    login_button = self.driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="LoginButton"]/android.view.ViewGroup[1]/android.view.View')
    email_field = self.driver.find_element_by_accessibility_id('EmailEntry')
    password_field = self.driver.find_element_by_accessibility_id('PasswordEntry')

    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()
    # Assert user has been navigated to the home page after logging in
    self.driver.implicitly_wait(10)
    self.assertTrue(self.driver.find_element_by_id('android:id/search_edit_frame').is_displayed())

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

def five_tap_for_enviroment(self):
    TouchAction(self.driver).tap(x=700, y=1900).perform()
    TouchAction(self.driver).tap(x=700, y=1900).perform()
    TouchAction(self.driver).tap(x=700, y=1900).perform()
    TouchAction(self.driver).tap(x=700, y=1900).perform()
    TouchAction(self.driver).tap(x=700, y=1900).perform()

def tap_code_to_switch_enviroments(self):
    TouchAction(self.driver).tap(x=210, y=370).perform()
    TouchAction(self.driver).tap(x=210, y=370).perform()
    TouchAction(self.driver).tap(x=1400, y=1400).perform()
    TouchAction(self.driver).tap(x=210, y=370).perform()
    TouchAction(self.driver).tap(x=210, y=370).perform()
    TouchAction(self.driver).tap(x=130, y=1300).perform()
    TouchAction(self.driver).tap(x=1300, y=330).perform()
    TouchAction(self.driver).tap(x=130, y=1300).perform()
    TouchAction(self.driver).tap(x=210, y=370).perform()
    TouchAction(self.driver).tap(x=1400, y=1400).perform()
    TouchAction(self.driver).tap(x=1300, y=330).perform()

def switch_enviroment(self):
    """
    Following Switching Enviroments test Case in Other Test SUite
    https://lncasoftware.ontestpad.com/script/1088#//
    """
    self.driver.hide_keyboard()
    self.driver.implicitly_wait(10)
    # Open the app.
    self.driver.find_element_by_xpath(l_page_ident).is_displayed()
    self.driver.implicitly_wait(10)
    # Rapidly click 5 times near the bottom of the window of the Login screen.
    five_tap_for_enviroment(self)
    
    self.driver.implicitly_wait(10)
    # Verify that an overlay with 4 buttons is displayed over the Login screen.
    """
    --The buttons are labelled as follows:
    |  1  |  2  |
    -------------
    |  3  |  4  |
    """
    # Verify that the overlay displays a box on the bottom of the window with the current environment (the default appears to be PROD, the other option available is DEV).
    self.assertTrue(visible_xpath_assert(self, element= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.Button'),'overlay is not displayed, error in trying to switch enviroment')
    find_by_text(self, text='DEV')
    print('Enviroment Switching is now available')

    # Click the following code on the buttons: 1 1 4 1 1 3 2 3 1 4 2.
    tap_code_to_switch_enviroments(self)

    self.driver.implicitly_wait(10)

    # Verify that the box on the bottom displays the new server. 
    self.assertTrue(self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.Button').is_displayed())
    find_by_text(self, text='PROD')
    print('Enviroment Has Now Been Switched To PROD')

    # Click the box on the bottom to close the overlay.
    click_text(self, text='PROD')
    self.driver.implicitly_wait(10)

    # Login using the correct credentials.
    self.assertTrue(self.driver.find_element_by_xpath(l_page_ident).is_displayed())

def help_check(self, help_msg):
    # Click the Help button.
    print('Click the Help button.')
    self.driver.find_element_by_xpath(d_help_box).click()
    print('>>  help btn clicked')
    
    # Verify that the correct Help popup is displayed.
    print('Verify that the correct Help popup is displayed.')
    self.driver.implicitly_wait(10)
    sites_help_text = self.driver.find_element_by_xpath(help_sites_msg).text
    self.assertEqual(sites_help_text, help_msg)
    print('>>  correct Help popup is displayed')   
    
    # select dismiss btn
    print('select dismiss btn')
    self.driver.find_element_by_xpath(help_dismiss_btn).click()
    print('>>  dismiss btn selected')

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

def update_cards(self):
    self.driver.implicitly_wait(5000)
    card_list = []
    xpath = '(//android.widget.TextView[@content-desc="ModifiedDateLabel"])['
    xpathend = "]"
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def city_cards(self):
    self.driver.implicitly_wait(5000)
    card_list = []
    xpath = '(//android.widget.TextView[@content-desc="CityLabel"])['
    xpathend = "]"
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def state_cards(self):
    self.driver.implicitly_wait(5000)
    card_list = []
    xpath = '(//android.widget.TextView[@content-desc="StateLabel"])['
    xpathend = "]"
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def category_title_card(self): 
    self.driver.implicitly_wait(10)
    card_list = []
    xpath = ''
    xpathend = ''
    for index in range(1, 20):
        path = f"{xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path)) > 0:
            self.driver.implicitly_wait(1)
            card_list.append(self.driver.find_element_by_xpath(f"{xpath}{index}{xpathend}").text)
        else:
            break
    return card_list

def holiday_title_card(self): 
    self.driver.implicitly_wait(10)
    card_list = []
    xpath = ''
    xpathend = ''
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
        item_type_list.append("LMRC-611MCC")
    elif item_type == "SW":
        item_type_list.append('LMSW-605')
        item_type_list.append('LMDM-601')
    elif item_type == "OS":
        item_type_list.append("LMPC-600")
        item_type_list.append("LMPX-600")
    elif item_type == "DL":
        item_type_list.append("LMDL-600")
    elif item_type == "LO":
        print('Loads Dont Exist Yet ^.^')
        
    return item_type_list

def user_logout(self):
    self.driver.implicitly_wait(10)
    self.driver.find_element_by_accessibility_id(m_logout_btn).click()
    logout_yes = self.driver.find_element_by_id('android:id/button1') 
    logout_yes.click()
    self.driver.implicitly_wait(10)

def user_settings(self):
    self.driver.implicitly_wait(10)
    if visible_xpath_assert(self, element= m_menu_btn2) == True:
        self.driver.find_element_by_xpath(m_menu_btn2).click()
    else:
        self.driver.find_element_by_xpath(m_menu_btn).click()

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
    self.driver.start_activity('us.legrand.fmui', activity)

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
    self.driver.start_activity('us.legrand.fmui', activity)

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

def city_assertion(self): 
    city_list = ["Pleasant Grove", "American Fork", "Orem"]
    city = self.driver.find_element_by_xpath(site_city_text).text
    print(city) 
    if city in city_list:
        print('Matches city name')      
    else: 
        raise AssertionError('City incorrect')
def state_func(self): 
    #set up 
    all_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    return all_states

def city_func(self): 
    all_cities = ["Pleasant Grove", "American Fork", "Orem", "PG", "AF"]
    return all_cities

def rv_card_items(self):
    self.driver.implicitly_wait(2000)
    card_xpath = '//android.view.ViewGroup[@content-desc="ScrollViewLocations"]/android.view.ViewGroup['
    card_xpath_end = ']/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View'
    card_title_xpath = '(//android.widget.TextView[@content-desc="TVTitleLabel"])['
    card_title_xpathend = "]"
    card_mac = '(//android.widget.TextView[@content-desc="MacAddress"])['
    card_mac_end = ']'
    card_signal = '(//android.view.View[@content-desc="SignalIcon"])['
    card_signal_end = ']'
    card_batt = '(//android.view.View[@content-desc="BatteryIcon"])['
    card_battend = ']'
    card_fav = '(//android.widget.Button[@content-desc="CheckLabel"])['
    card_fav_end = ']'
    card_find_device = '(//android.widget.Button[@content-desc="DeviceIdentifyBtn"])['
    card_find_device_end = ']'
    for index in range(1, 20):
        card_path = f"{card_xpath}{index}{card_xpath_end}"
        card_titles = f'{card_title_xpath}{index}{card_title_xpathend}'
        card_mac_path = f'{card_mac}{index}{card_mac_end}'
        card_signal_path = f'{card_signal}{index}{card_signal_end}'
        card_batt_path = f'{card_batt}{index}{card_battend}'
        card_fav_path = f'{card_fav}{index}{card_fav_end}'
        card_find_device_path = f'{card_find_device}{index}{card_find_device_end}'
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, card_path)) > 0:
            self.driver.implicitly_wait(1)
            visible_xpath_assert(self, element= card_titles)
            visible_xpath_assert(self, element= card_mac_path)
            visible_xpath_assert(self, element= card_signal_path)
            device_name = self.driver.find_element_by_xpath(card_titles).text
            if not device_name == 'LMRC-611MCC':
                print('Leaf Device Found')
                self.driver.find_element_by_xpath(card_titles).click()
                self.driver.implicitly_wait(10)
                self.assertTrue(visible_accessibility_id_assert(self, element= rv_drawer_ident))
                self.assertTrue(visible_accessibility_id_assert(self, element= rv_drawer_device_batt))
                TouchAction(self.driver).tap(x=200, y=1080).perform()                
                visible_xpath_assert(self, element= card_fav_path)
                visible_xpath_assert(self, element= card_find_device_path)
            else:
                print('LMRC Found')
                self.driver.find_element_by_xpath(card_titles).click()
                self.driver.implicitly_wait(500)
                self.assertTrue(visible_accessibility_id_assert(self, element= rv_drawer_ident))
                self.assertFalse(visible_accessibility_id_assert(self, element= rv_drawer_device_batt))
                TouchAction(self.driver).tap(x=200, y=1080).perform()
                print('no battery place holder found')
                visible_xpath_assert(self, element= card_fav_path)
                visible_xpath_assert(self, element= card_find_device_path)

def search_results(self, text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False

def help_check(self, help_msg):
    # Click the Help button.
    print('Click the Help button.')
    self.driver.find_element_by_xpath(d_help_box).click()
    print('>>  help btn clicked')
    
    # Verify that the correct Help popup is displayed.
    print('Verify that the correct Help popup is displayed.')
    self.driver.implicitly_wait(10)
    sites_help_text = self.driver.find_element_by_xpath(help_sites_msg).text
    self.assertEqual(sites_help_text, help_msg)
    print('>>  correct Help popup is displayed')   
    
    # select dismiss btn
    print('select dismiss btn')
    self.driver.find_element_by_accessibility_id(help_dismiss_btn).click()
    print('>>  dismiss btn selected')