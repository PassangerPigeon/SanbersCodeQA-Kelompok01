import unittest
import time
from selenium.webdriver.common.by import By
from POM.loginPOM import loginPage

def testlogin(self, driver):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addUsername).send_keys("adhit") # isi email
        driver.find_element(*loginPage.addPassword).send_keys("12345") # isi password
        driver.find_element(*loginPage.loginClick).click()
        # validasi
        time.sleep(3)
        response_data = driver.find_element(By.ID,'nameofuser').text
        self.assertIn('Welcome ', response_data)
        
def testFailedloginUserNotExist(self, driver, username, password):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addUsername).send_keys(username) # isi email
        driver.find_element(*loginPage.addPassword).send_keys(password) # isi password
        driver.find_element(*loginPage.loginClick).click()
        #validasi
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('User does not exist', alert_data)
        alert.accept
        
def testFailedloginWrongPass(self, driver, username, password):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addUsername).send_keys(username) # isi email
        driver.find_element(*loginPage.addPassword).send_keys(password) # isi password
        driver.find_element(*loginPage.loginClick).click()
        #validasi
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Wrong password', alert_data)
        alert.accept
        
def testLogout(self, driver):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addUsername).send_keys("adhit") # isi email
        driver.find_element(*loginPage.addPassword).send_keys("12345") # isi password
        driver.find_element(*loginPage.loginClick).click()
        # validasi
        time.sleep(3)
        driver.find_element(By.ID,"logout2").click()
        response_data = driver.find_element(By.ID,'login2').text
        self.assertIn('Log in', response_data)
        
def testFailedloginNoUsername(self, driver):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addPassword).send_keys("12345") # isi password
        driver.find_element(*loginPage.loginClick).click()
        #validasi
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Please fill out Username and Password', alert_data)
        alert.accept
        
def testFailedloginNoPassword(self, driver):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(*loginPage.addUsername).send_keys("adhit") # isi password
        driver.find_element(*loginPage.loginClick).click()
        #validasi
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Please fill out Username and Password', alert_data)
        alert.accept