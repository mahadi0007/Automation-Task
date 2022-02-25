from Locators.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.locator = CreateAccountLocators
        self.timer = 60


    def enter_email(self,email):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ENTER_EMAIL)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.ENTER_EMAIL)).send_keys(email)

    def enter_pass(self,password):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.PASSWORD)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.PASSWORD)).send_keys(password)

    def click_signin(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.SIGN_IN_BUTTON)).click()

    def enter_reg_email(self,email):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.REGISTER_EMAIL_BUTTON)).clear()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.REGISTER_EMAIL_BUTTON)).send_keys(email)

    def click_create_acc(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.CREATE_ACCOUNT_BTN)).click()
