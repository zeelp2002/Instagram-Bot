from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time

#Put username and password of account here
USERNAME = 'username'
PASSWORD = 'password'

#Change if you would like notifications on or off
switch = False


class InstagramBot:
    
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.url = 'https://www.instagram.com/'

        self.driver = webdriver.Chrome('chromedriver.exe')
        
        self.login()
        time.sleep(2)
        self.findUser('zeel2002')
        time.sleep(3)
        self.followUser
        


    def login(self):
        self.driver.get('{}accounts/login/'.format(self.url))

        #Finds elements by name and puts in username and password in textbox
        enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        
        #Login after the username and passoword is entered, waits for page to fully load
        loginBtn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button/div')
        time.sleep(0.1)
        loginBtn.click()

        time.sleep(2)

        #Saves the Users info 
        saveUserBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        time.sleep(1)
        saveUserBtn.click()

        time.sleep(1)

        #Sets the user to receive or not receive notifications
        if switch == True:
            saveUserBtn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
            time.sleep(1)
        else:
            saveUserBtn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            time.sleep(1)
        
        
    def findUser(self, user):
        self.driver.get('{}{}/'.format(self.url, user))

    def followUser(self):
        followBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/button')
        followBtn.click()
        
if __name__ == '__main__':
    ig_bot = InstagramBot(USERNAME, PASSWORD)
    

    
