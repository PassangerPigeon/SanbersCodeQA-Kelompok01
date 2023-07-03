from selenium.webdriver.common.by import By

class PlaceOrder():
    selectProduct1 = (By.XPATH,'//*[@id="tbodyid"]/div[1]/div/a')
    selectProduct2 = (By.XPATH,'//*[@id="tbodyid"]/div[2]/div/a')
    addToCart1 = (By.CSS_SELECTOR,"[onclick='addToCart(1)']")
    addToCart2 = (By.CSS_SELECTOR,"[onclick='addToCart(2)']")
    clickHomeMenu = (By.XPATH,'//*[@id="navbarExample"]/ul/li[1]/a')
    clickCartMenu = (By.ID,"cartur")
    clickPlaceOrder = (By.XPATH,'//*[@id="page-wrapper"]/div/div[2]/button')
    purchaseButton = (By.CSS_SELECTOR,"[onclick='purchaseOrder()']")
    okButton = (By.CSS_SELECTOR,"[onclick='purchaseOrder()']")
    thankYouText = (By.XPATH,'/html/body/div[10]/h2')