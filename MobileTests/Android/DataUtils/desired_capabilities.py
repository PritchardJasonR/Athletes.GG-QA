import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

def des_cap(self):
    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )
    desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": 'Android',
    "app": PATH('..\\Resources\\gg.athletes.apk'),
    "appPackage": "gg.athletes.app",
    "appWaitActivity": "*",
    "autoGrantPermissions": "true",
    "ignoreUnimportantViews": "true",
    "newCommandTimeout": "20", #seconds
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    
    return driver

def no_reset_caps(self):

    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )

    desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": 'Android',
    "app": PATH('..\\Resources\\gg.athletes.apk'),
    "appPackage": "gg.athletes.app",
    "appWaitActivity": "*",
    "autoGrantPermissions": "true",
    "ignoreUnimportantViews": "true",
    "noReset": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)

    return driver

def play_store_caps(self):
    desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "appPackage": "com.android.vending",
    "appWaitActivity": ".AssetBrowserActivity",
    "autoGrantPermissions": "true",
    "ignoreUnimportantViews": "true",
    "deviceName": "Android",
    "noReset": "true",
    "appActivity": ".AssetBrowserActivity",
    "uninstallOtherPackages": "gg.athletes.app"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)

    return driver