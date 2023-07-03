from selenium.webdriver.common.by import By

class PlaceOrder():
    selectProduct = (By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
    addToCart = (By.CSS_SELECTOR,"[onclick='addToCart(1)']")
    clickCartMenu = (By.ID,"cartur")
    clickPlaceOrder = (By.XPATH,'//*[@id="page-wrapper"]/div/div[2]/button')
    purchaseButton = (By.CSS_SELECTOR,"[onclick='purchaseOrder()']")
    okButton = (By.CSS_SELECTOR,"[onclick='purchaseOrder()']")
    thankYouText = (By.XPATH,'/html/body/div[10]/h2')