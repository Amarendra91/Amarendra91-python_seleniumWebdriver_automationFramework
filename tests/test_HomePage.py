import pytest

from TestData.HomePageData import HomePageTestData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["name"])  # Data driven mechanism to avoid hard coding
        log.info("Name is :" + getData["name"])
        homePage.getEmail().send_keys(getData["mail"])  # Data driven mechanism to avoid hard coding
        log.info("Email is :" + getData["mail"])
        homePage.getPasswd().send_keys(getData["pwd"])  # Data driven mechanism to avoid hard coding
        homePage.getCheckbox().click()
        self.selectValue(homePage.getGender(), getData["gender"])  # Data driven mechanism to avoid hard coding
        log.info("Person is :" + getData["gender"])
        homePage.getStatus().click()
        homePage.getDOB().send_keys(getData["birthday"])  # Data driven mechanism to avoid hard coding
        log.info(getData["name"] + "`s " + " D.O.B is " + getData["birthday"])
        homePage.clickSubmit().click()
        alertText = homePage.checkSubmission().text
        assert ("Success" in alertText)
        homePage.messageClosure().click()
        self.driver.refresh()

    #  Test parameterization achieved using the fixture by calling it's associated method into above test case
    @pytest.fixture(params=HomePageTestData.test_Data)  # Test data came from other package
    def getData(self, request):
        return request.param
