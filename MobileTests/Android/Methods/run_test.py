import os
import traceback
import datetime
from time import sleep
from appium import webdriver

def test_run(test_name, passes, fails, trace):

    try:
        os.system('start cmd /r appium')
        test_name()
        os.system('taskkill /IM cmd.exe /FI "WINDOWTITLE eq C:\Windows\system32\cmd.exe"')
        passes.append({test_name.__name__})
        print(f'============== Test {test_name.__name__} PASSED!!!!!')
    except Exception as e:
        print('**************************************************************************************************************')
        print(f'<><> TEST {test_name.__name__}FAILED <><>\n')
        os.system('taskkill /IM cmd.exe /FI "WINDOWTITLE eq C:\Windows\system32\cmd.exe"')
        fails.append(test_name.__name__)
        trace.append(e.__traceback__)