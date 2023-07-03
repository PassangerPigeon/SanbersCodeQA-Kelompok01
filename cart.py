import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToChart(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # webdriver.Chrome(ChromeDriverManager().install())
        
        self.url = "https://www.demoblaze.com/"
    def test_add_to_chart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)

        driver.find_element(By.XPATH, "/html//div[@id='tbodyid']/div[1]//h4/a[@href='prod.html?idp_=1']").click()
        driver.find_element(By.XPATH, "/html//div[@id='tbodyid']//a[@href='#']").click()
        
        alert = driver.switch_to.alert
        self.assertIn('Product added', alert.text)
        alert.accept()
        time.sleep(5)

    def test_delete_from_chart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get(self.url)

        driver.find_element(By.XPATH, "/html//div[@id='tbodyid']/div[1]//h4/a[@href='prod.html?idp_=1']").click()
        driver.find_element(By.XPATH, "/html//div[@id='tbodyid']//a[@href='#']").click()
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.XPATH, "/html//a[@id='cartur']").click()
        driver.find_element(By.XPATH, "/html//tbody[@id='tbodyid']//a[@href='#']").click()
        cart = driver.find_element(By.CLASS_NAME, "panel-title").text
        self.assertEquals(cart,"")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()