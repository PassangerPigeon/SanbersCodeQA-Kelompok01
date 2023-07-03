import unittest
import time
from selenium.webdriver.common.by import By
from POM.placeOrderPOM import PlaceOrder

def testPlaceOrder(self, driver):
        # steps
        driver.find_element(*PlaceOrder.selectProduct).click()
        time.sleep(2)
        driver.find_element(*PlaceOrder.addToCart).click() # add to cart
        time.sleep(3)
        alert = driver.switch_to.alert
        alert_data = alert.text
        self.assertIn('Product added', alert_data)
        alert.accept() # OK modal
        driver.find_element(*PlaceOrder.clickCartMenu).click() # click cart menu
        time.sleep(4)
        driver.find_element(*PlaceOrder.clickPlaceOrder).click() # place order
        time.sleep(2)
        driver.find_element(By.ID,"name").send_keys('Ians')
        driver.find_element(By.ID,"country").send_keys('Indonesia')
        driver.find_element(By.ID,"city").send_keys('Jakarta')
        driver.find_element(By.ID,"card").send_keys('12345678910')
        driver.find_element(By.ID,"month").send_keys('09')
        driver.find_element(By.ID,"year").send_keys('2024')
        driver.find_element(*PlaceOrder.purchaseButton).click()
               
        # validasi
        time.sleep(3)
        tytext = driver.find_element(*PlaceOrder.thankYouText).text
        self.assertIn('Thank you for your purchase!', tytext)
        driver.find_element(*PlaceOrder.okButton).click()
        