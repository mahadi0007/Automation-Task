from Locators.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.locator = HomeLocators
        self.timer = 60



    def click_signin(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SIGN_IN_BTN_NAME)).click()
