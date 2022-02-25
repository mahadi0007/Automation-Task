from selenium.webdriver import ActionChains
from time import sleep
from Locators.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AddToCart():

    def __init__(self, driver):
        self.driver = driver
        self.locator = AddToCartlocators
        self.timer = 60

    def add_causal_dress_to_cart(self):
        action = ActionChains(self.driver)

        action.move_to_element(WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.CASUAL_DRESS))).perform()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.CASUAL_DRESS_ADDCART_BTN)).click()
        self.driver.implicitly_wait(5)

    def click_continue_shoppingt(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.continue_shopping_btn)).click()
        self.driver.implicitly_wait(10)

    def add_tshirt_to_cart(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.tshirt_page_btn)).click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.filter)).click()
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        action.move_to_element(WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.tshirt_card))).perform()
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.tshirt_addtocart_btn)).click()
        self.driver.implicitly_wait(5)

    def checkout_cart(self):
        WebDriverWait(self.driver, self.timer).until(
            EC.element_to_be_clickable(self.locator.checkout_cart_btn)).click()
        sleep(2)
