
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        baseLogin.testlogin(self, driver)
        
    def test_b_failed_login_user_not_exist(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        baseLogin.testFailedloginUserNotExist(self, driver,'adhitx','12345')

    def test_c_failed_login_wrong_pass(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        time.sleep(3)
        baseLogin.testFailedloginWrongPass(self, driver,'adhit','54321')


if __name__ == "__main__":
    unittest.main()