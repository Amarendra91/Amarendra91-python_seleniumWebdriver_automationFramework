from selenium.webdriver.common.by import By

from pageObjects.OrderPage import OrderPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    addProduct = (By.XPATH, "//div[@class='card h-100']/div/button")
    checkoutStart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutEnd = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.productTitle)

    def addToCart(self):
        return self.driver.find_element(*CheckoutPage.addProduct)

    def initiateCheckout(self):
        return self.driver.find_element(*CheckoutPage.checkoutStart)

    def completeCheckout(self):
        self.driver.find_element(*CheckoutPage.checkoutEnd).click()
        orderPage = OrderPage(self.driver)
        return orderPage
