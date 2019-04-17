from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 


print('--------------------------')

driver = webdriver.Firefox()

driver.implicitly_wait(5)
    ## implicity_wait makes the bot wait 5 seconds before every action
    ## so the site content can load up
    

# Define the functions
def login_to_accessqa (username, userpass):
	## Open the login page
    driver.get('https://accessibilityqa.codemantra.com')

    ## Log the details
    print(username + " is logging into accessQA.")


    ## Find the fields and log into the account. 
    textfield_username = driver.find_element_by_id('user001')
    print(textfield_username)
    textfield_username.clear()
    textfield_username.send_keys(username)

    textfield_email = driver.find_element_by_id('pas001')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_id('save_sla')
    submit_button.click()

    ## Log the details
    print(username + " is logged in! -> QA")

# Define the functions
def login_to_accessdev (username, userpass):
	## Open the login page
    driver.get('https://accessibilitydev.codemantra.com')

    ## Log the details
    print(username + " is logging into accessDev.")


    ## Find the fields and log into the account. 
    textfield_username = driver.find_element_by_id('user001')
    print(textfield_username)
    textfield_username.clear()
    textfield_username.send_keys(username)

    textfield_email = driver.find_element_by_id('pas001')
    textfield_email.clear()
    textfield_email.send_keys(userpass)

    submit_button = driver.find_element_by_id('save_sla')
    submit_button.click()

    ## Log the details
    print(username + " is logged in! -> QA")


def login_to_expressqa (username, userpass):

    ## Open the login page
    driver.get('https://accessibilityexpressqa.codemantra.com')    

    ## Log the details
    print(username + " is logging into expressqa.")
    
    ## Find the fields and log into the account. 
    textfield_username = driver.find_element_by_id('email_id')
    textfield_username.clear()
    textfield_username.send_keys(username) 

    submit_button = driver.find_element_by_class_name('next')
    submit_button.click()

    ## Log the details
    print(username + " is logged in! -> expressqa")

    time.sleep(10)

    textfield_username = driver.find_element_by_id('pas001')
    textfield_username.clear()
    textfield_username.send_keys(userpass) 
    

    submit_button = driver.find_element_by_id('LoginPass')
    submit_button.click()


## Define the user and email combo. 

login_to_accessqa("karthikj@codemantra.co.in", "Test#222")

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to.window(Window_List[-1]);

login_to_accessdev("karthikj@codemantra.co.in", "Test#222")

time.sleep(2)
driver.execute_script("window.open('');")
Window_List = driver.window_handles
driver.switch_to.window(Window_List[-1]);


login_to_expressqa("shahid@codemantra.in", "Test#222")



## wait for 2 seconds
time.sleep(2)


print("task complete")
