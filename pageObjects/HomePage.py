
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employmentStatus = (By.ID, "inlineRadio1")
    birthDate = (By.NAME, "bday")
    submitAction = (By.CSS_SELECTOR, "input[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")
    crossSuccessMsg = (By.CLASS_NAME, "close")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPasswd(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getStatus(self):
        return self.driver.find_element(*HomePage.employmentStatus)

    def getDOB(self):
        return self.driver.find_element(*HomePage.birthDate)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submitAction)

    def checkSubmission(self):
        return self.driver.find_element(*HomePage.successMessage)

    def messageClosure(self):
        return self.driver.find_element(*HomePage.crossSuccessMsg)

    def shopItems(self):
        # Page Object Mechanism used instead  of driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        # CheckoutPage class object created,linked to CheckoutPage class constructor to parse driver
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage
