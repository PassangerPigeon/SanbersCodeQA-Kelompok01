import unittest
import time
from selenium.webdriver.common.by import By

def testPlaceOrder(self, driver):
        # steps
        driver.find_element(By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"[onclick='addToCart(1)']").click() # add to cart
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Product added', alert_data)
        alert.accept() # OK modal
        driver.find_element(By.ID,"cartur").click() # click cart menu
        time.sleep(4)
        driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div/div[2]/button').click() # place order
        time.sleep(2)
        driver.find_element(By.ID,"name").send_keys('Ians')
        driver.find_element(By.ID,"country").send_keys('Indonesia')
        driver.find_element(By.ID,"city").send_keys('Jakarta')
        driver.find_element(By.ID,"card").send_keys('12345678910')
        driver.find_element(By.ID,"month").send_keys('09')
        driver.find_element(By.ID,"year").send_keys('2024')
        driver.find_element(By.CSS_SELECTOR,"[onclick='purchaseOrder()']").click()
               
        # validasi
        respone_data = driver.find_element(By.TAG_NAME,'h2').text()
        self.assertIn('Thank you for your purchase!', respone_data)
        driver.find_element(By.CLASS_NAME,'confirm btn btn-lg btn-primary').click()
        