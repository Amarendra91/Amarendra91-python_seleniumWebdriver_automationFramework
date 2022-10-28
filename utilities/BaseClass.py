import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        # explicit wait utility
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectValue(self, locator, text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # testcase / method name reference
        # reference to file location where logging info will be stored
        fileHandler = logging.FileHandler(
            "C:/Users/amare/PycharmProjects/WebAutomationFrameworkDesign[Python,Selenium]/utilities/logfile.log")
        # specify the format to store the information in the log file as per requirement
        formatter = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)  # reference to logging format
        logger.setLevel(logging.INFO)  # set hierarchy of log information to be be displayed as mentioned below
        logger.addHandler(fileHandler)  # fileHandler object reference given to the logger object
        return logger
