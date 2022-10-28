from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    countryDropDown = (By.CSS_SELECTOR, "#country")
    countryName = (By.LINK_TEXT, "India")
    checkConditions = (By.CLASS_NAME, "checkbox-primary")
    purchaseItems = (By.CSS_SELECTOR, "input[type='submit']")
    checkOrderConfirmation = (By.CLASS_NAME, "alert-success")
    crossSuccessMsg = (By.CSS_SELECTOR, "a[class='close']")

    def searchCountry(self):
        return self.driver.find_element(*OrderPage.countryDropDown)

    def selectCountry(self):
        return self.driver.find_element(*OrderPage.countryName)

    def checkTerms(self):
        return self.driver.find_element(*OrderPage.checkConditions)

    def placeOrder(self):
        return self.driver.find_element(*OrderPage.purchaseItems)

    def orderConfirmation(self):
        return self.driver.find_element(*OrderPage.checkOrderConfirmation)

    def messageClosure(self):
        return self.driver.find_element(*OrderPage.crossSuccessMsg)
