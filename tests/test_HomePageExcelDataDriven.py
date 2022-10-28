import pytest

from TestData.HomePageData import HomePageTestData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):

    def test_formSubmission(self, getData, getDate):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["name"])  # Data driven mechanism to avoid hard coding
        log.info("Name is :" + getData["name"])
        homePage.getEmail().send_keys(getData["mail"])  # Data driven mechanism to avoid hard coding
        log.info("Email is :" + getData["mail"])
        homePage.getPasswd().send_keys(getData["pwd"])  # Data driven mechanism to avoid hard coding
        log.info("Password is :"+str(getData["pwd"]))
        homePage.getCheckbox().click()
        self.selectValue(homePage.getGender(), getData["gender"])  # Data driven mechanism to avoid hard coding
        log.info("Person is :" + getData["gender"])
        homePage.getStatus().click()
        homePage.getDOB().send_keys(getDate["birthday"])  # Data driven mechanism to avoid hard coding
        log.info(getData["name"] + "`s " + " D.O.B is " + getDate["birthday"])
        homePage.clickSubmit().click()
        alertText = homePage.checkSubmission().text
        assert ("Success" in alertText)
        homePage.messageClosure().click()
        self.driver.refresh()

    #  Test parameterization achieved using the fixture by calling it's associated method into above test case
    @pytest.fixture(params=HomePageTestData.getUserData("user1"))  # Test data came from Excel sheet
    def getData(self, request):
        return request.param

    @pytest.fixture(params=HomePageTestData.date)  # Test data came from custom dictionary variable
    def getDate(self, request):
        return request.param
