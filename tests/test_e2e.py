import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass  # Using Inheritance to use fixture as optimization


class TestShopping(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # HomePage class object created and linked to HomePage class constructor to parse driver object from this test
        homePage = HomePage(self.driver)
        # link the checkOutPage class object into HomePage class under shopItems method for optimization
        checkOutPage = homePage.shopItems()
        # -- Implicit wait
        self.driver.implicitly_wait(4)

        # -- Scroll through product Card Body section
        self.driver.execute_script("window.scrollBy(0,500);")

        # Page Object Mechanism used instead  of driver.find_elements(By.XPATH,"//div[@class='card h-100']/div/h4/a")
        productTitles = checkOutPage.getProductTitles()  # common locator used to fetch all product title
        log.info("All product details collected.")
        # looking for blackberry product title and then add that to cart for checkout
        for title in productTitles:
            log.info(title.text)
            if title == "Blackberry":
                checkOutPage.addToCart().click()

        # proceed to check out
        checkOutPage.initiateCheckout().click()
        # link the confirmPage class object into checkOutPage class under checkOutItems method for optimization
        orderPage = checkOutPage.completeCheckout()
        # Auto suggest dropdown component handling
        orderPage.searchCountry().send_keys("Ind")
        log.info("Entering the key word Ind to search the country")
        self.verifyLinkPresence("India")  # Explicit wait implemented as utility in BaseClass
        time.sleep(3)
        orderPage.selectCountry().click()

        # -- click on the terms & conditions checkbox
        orderPage.checkTerms().click()

        # -- click on the purchase button
        orderPage.placeOrder().click()

        # Purchase successful text visible and apply partial Assertion to verify the message displayed correctly or not
        successText = orderPage.orderConfirmation().text
        log.info(successText)
        assert "Success! Thank you!" in successText

        # -- close the order successful message
        orderPage.messageClosure().click()
