from Locators.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckoutPage():

    def __init__(self,driver):
        self.driver = driver

        self.locator = CheckoutPagelocators
        self.timer = 60


    def click_summery_proceed_to_checkout(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SUMMARY_PROCEED_BTN)).click()

    def click_address_proceed_to_checkout(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ADDRESS_PROCEED_BTN)).click()

    def click_shipping_proceed_to_checkout(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.TOS_CHECKBOX_ID)).click()

        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SHIPPING_PROCEED_BTN_NAME)).click()

    def payment(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.PAYMENT_PAY_BE_CHECK_BTN)).click()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.CONFIRM_ORDER_BTN)).click()

        self.driver.implicitly_wait(5)

