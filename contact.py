import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

class TestContactMenu(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.demoblaze.com/"
    def test_submit_contact_menu(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)
       
        driver.find_element(By.XPATH, "//div[@id='navbarExample']/ul/li[2]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.ID,"recipient-email").send_keys("eliindah6@gmail.com") # isi email 
        driver.find_element(By.ID,"recipient-name").send_keys("eliindah") # isi name 
        driver.find_element(By.ID,"message-text").send_keys("marketplace which is easy and convenient to use") # isi message  
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(1)
        
        alert = driver.switch_to.alert
        print(alert.text)
        self.assertIn('Thanks for the message!!', alert.text)
        alert.accept()

    def test_fail_submit_contact_menu(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)
       
        driver.find_element(By.XPATH, "//div[@id='navbarExample']/ul/li[2]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.ID,"recipient-email").send_keys("cba123@") # isi email 
        driver.find_element(By.ID,"recipient-name").send_keys("12345") # isi name 
        driver.find_element(By.ID,"message-text").send_keys("xxxxx") # isi message  
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(1)

     
        alert = driver.switch_to.alert
        print(alert.text)
        self.assertIn('Thanks for the message!!', alert.text)
        alert.accept()
        # alert = Alert(driver)
        # alert.accept()

    def test_empty_name_submit_contact_menu(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)
       
        driver.find_element(By.XPATH, "//div[@id='navbarExample']/ul/li[2]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.ID,"recipient-email").send_keys("eliindah6@gmail.com") # isi email 
        driver.find_element(By.ID,"recipient-name").send_keys("") # isi name 
        driver.find_element(By.ID,"message-text").send_keys("") # isi message  
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(1)

     
        alert = driver.switch_to.alert
        print(alert.text)
        self.assertIn('Thanks for the message!!', alert.text)
        alert.accept()
        # alert = Alert(driver)
        # alert.accept()
        
    def test_empty_all_submit_contact_menu(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)
       
        driver.find_element(By.XPATH, "//div[@id='navbarExample']/ul/li[2]/a[@href='#']").click()
        time.sleep(2)
        driver.find_element(By.ID,"recipient-email").send_keys("") # isi email 
        driver.find_element(By.ID,"recipient-name").send_keys("") # isi name 
        driver.find_element(By.ID,"message-text").send_keys("") # isi message  
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='exampleModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(1)

     
        alert = driver.switch_to.alert
        print(alert.text)
        self.assertIn('Thanks for the message!!', alert.text)
        alert.accept()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()