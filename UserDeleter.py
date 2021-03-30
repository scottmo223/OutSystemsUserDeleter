import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

username = input("Username: ")
password = input("Password: ")

driver = webdriver.Chrome('../chromedriver')  # path to chromedriver.exe
driver.get('https://applydev.mercyships.org/users')

time.sleep(15)

#login
usernameField = driver.find_element_by_name('wt37$wtLogin$wtUserNameInput')
passwordField = driver.find_element_by_name('wt37$wtLogin$wtPasswordInput')
submitButton = driver.find_element_by_name('wt37$wtLogin$wtLoginButton')

usernameField.clear()
passwordField.clear()
usernameField.send_keys(username)
passwordField.send_keys(password)
time.sleep(5)

submitButton.send_keys(Keys.RETURN)

#userids
userIds = [1910, 1939]

#loop through userids and append to url: https://applydev.mercyships.org/users/User_Show.aspx?UserId=1910
for userId in userIds:
    driver.get('https://applydev.mercyships.org/users/User_Show.aspx?UserId='+str(userId))
    delete = input("delete? y/n: ")
    if(delete == 'y'):
        deleteButton = driver.find_element_by_id('wt69_wtTitle_wt94')
        deleteButton.send_keys(Keys.RETURN)
        time.sleep(2)
    else:
        pass

print('Done!')

driver.quit()