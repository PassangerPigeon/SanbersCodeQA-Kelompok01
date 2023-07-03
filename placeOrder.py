
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import basePlaceOrder


class TestPlaceOrder(unittest.TestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    def test_a_place_order(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceOrder(self, driver)
        
    def test_b_place_two_order(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceTwoOrder(self, driver)
    
    def test_c_place_empty_order(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceEmptyOrder(self, driver)
        
    def test_d_place_order_name_only(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceOrderNameOnly(self, driver)
        
    def test_e_place_order_card_only(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceOrderCardOnly(self, driver)
        
    def test_f_place_order_card_only(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        basePlaceOrder.testPlaceOrderNameandCreditOnly(self, driver)

if __name__ == "__main__":
    unittest.main()