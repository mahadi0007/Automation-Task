from selenium.webdriver import ActionChains
from Locators.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class MyAccountPage():

    def __init__(self,driver):
        self.driver = driver

        self.locator = MyAccountPageLocator
        self.timer = 60

    def click_signout(self):

        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SIGN_OUT_BTN_NAME)).click()

    def click_casual_dress(self):
        action = ActionChains(self.driver)

        action.move_to_element(
            WebDriverWait(self.driver, self.timer).until(
                EC.element_to_be_clickable(self.locator.DRESS_BTN))
        ).perform()

        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SIGN_OUT_BTN_NAME)).click()

