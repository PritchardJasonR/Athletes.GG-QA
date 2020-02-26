import os
import traceback
import datetime
import time
# Import tests   FileName as Class
import TestSuite.SearchAthlete as SearchAthleteTest
import TestSuite.Login as LoginTest
import TestSuite.GetTheApp as GetTheAppTest
import TestSuite.LoginSearchLoad as LoginSearchLoadTest
import TestSuite.SearchEvent as SearchEvent
import TestSuite.SearchGames as SearchGames
import TestSuite.SearchChar as SearchChar
#End of Test Imports
from Methods.run_test import test_run
from time import sleep
# Returns abs path relative to this file instead of cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
start = time.time()
passes = []
fails = []
trace = []
tests = [
    # Example test account creation  Class.Class()method
    
    #Get The App Test
    GetTheAppTest.GetTheAppTest().testGetTheApp,

    # #Login Test
    LoginTest.LoginTest().testLogin,

    # Search Athlete Test
    SearchAthleteTest.SearchAthleteTest().testSearchAthlete,

    # Search Event Test
    SearchEvent.SearchEventTest().testSearchEvent,

    # Search Games
    SearchGames.SearchGamesTest().testSearchGames,

    # Search Char
    SearchChar.SearchCharTest().testSearchChar

]

for test in tests:
    test_run(test, passes, fails, trace)

end = time.time()
# Reporting Test Results
p = len(passes)
f = len(fails)
t = p + f
print(f'Seconds Tests took to run{end - start}')
now = datetime.datetime.now()
filename = f'agg.android.testrun{now.strftime("%Y-%m-%d_%H-%M")}' #change this to however you want it to look (but no :'s or /'s since windows doesn't like those)
with open(PATH(f"executions/{filename}.txt"),'w') as result:
    result.write('[][][][][][][][][][ TEST RESULTS ][][][][][][][][][][]][][][][][]\n\n')
    result.write(f'Tests took {end - start} Seconds to run\n\n')
    result.write(f'Out of {t} tests ran, {p} passed and {f} failed\n\n')
    result.write(f'tests that passed{passes}\n\n')
    result.write(f'tests that failed {fails}\n\n')
    result.write(' >>>>>>>   Tracebacks   <<<<<<<<<<\n')
    for item in trace:
        result.write(f'******************* Start Trace  *****************************\n\n')
        myList = traceback.format_tb(item)
        for row in myList:
            result.write(str(row))
        result.write('\n')
        result.write('******************* END TRACE *******************************\n\n')
print('[][][][][][][][][][ TEST RESULTS ][][][][][][][][][][]][][][][][]\n\n')
print(f'Out of {t} tests ran, {p} passed and {f} failed\n\n')
print(f'tests that passed{passes}')
print('\n')
print(f'tests that failed {fails}')
print('\n')
print(' >>>>>>>   Tracebacks   <<<<<<<<<<')
for item in trace:
    print('*******************Start Trace *****************************\n\n')
    traceback.print_tb(item)
    print('*******************END TRACE *******************************\n\n')
