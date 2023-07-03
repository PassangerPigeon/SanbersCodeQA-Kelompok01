import unittest
import time
from selenium.webdriver.common.by import By

def testlogin(self, driver):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(By.ID,"loginusername").send_keys("adhit") # isi email
        driver.find_element(By.ID,"loginpassword").send_keys("12345") # isi password
        driver.find_element(By.CSS_SELECTOR,"[onclick='logIn()']").click()
        # validasi
        time.sleep(3)
        response_data = driver.find_element(By.ID,'nameofuser').text
        self.assertIn('Welcome ', response_data)
        
def testFailedloginUserNotExist(self, driver, username, password):
        # steps
        driver.find_element(By.ID,"login2").click()
        time.sleep(2)
        driver.find_element(By.ID,"loginusername").send_keys(username) # isi email
        driver.find_element(By.ID,"loginpassword").send_keys(password) # isi password
        driver.find_element(By.CSS_SELECTOR,"[onclick='logIn()']").click()
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
        driver.find_element(By.ID,"loginusername").send_keys(username) # isi email
        driver.find_element(By.ID,"loginpassword").send_keys(password) # isi password
        driver.find_element(By.CSS_SELECTOR,"[onclick='logIn()']").click()
        #validasi
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Wrong assword', alert_data)
        alert.accept
     