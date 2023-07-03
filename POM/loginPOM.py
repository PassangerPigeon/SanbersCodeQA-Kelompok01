from selenium.webdriver.common.by import By

class loginPage():
    username = "loginusername"
    passw = "loginpassword"
    loginClick = (By.CSS_SELECTOR,"[onclick='logIn()']")
    
    addUsername = (By.ID,username)
    addPassword = (By.ID,passw)