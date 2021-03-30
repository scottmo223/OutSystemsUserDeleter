import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import urllib.request

username = input("Username: ")
password = input("Password: ")

driver = webdriver.Chrome('../chromedriver')  # path to chromedriver.exe
driver.get('https://apply.mercyships.org/users')

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
userIds = [
    83443,
    83417,
    83400,
    83439,
    83410,
    83428,
    83392,
    83388,
    83431,
    83444,
    83404,
    83384,
    83415,
    83403,
    83390,
    83405,
    83381,
    83383,
    83407,
    83406,
    83434,
    83442,
    83401,
    83412,
    83426,
    83418,
    83378,
    83413,
    83382,
    83441,
    83385,
    83389,
    83424,
    83380,
    83402,
    83445,
    83409
]

#loop through userids and append to url: https://applydev.mercyships.org/users/User_Show.aspx?UserId=1910
for userId in userIds:
    driver.get('https://apply.mercyships.org/users/User_Show.aspx?UserId='+str(userId))
    delete = input("delete? y/n: ")
    if(delete == 'y'):
        deleteButton = driver.find_element_by_id('wt69_wtTitle_wt83_wt5')
        deleteButton.send_keys(Keys.RETURN)
        Alert(driver).accept()
        time.sleep(3)
    else:
        pass

print('Done!')

driver.quit()