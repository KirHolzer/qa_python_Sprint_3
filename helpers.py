from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestData

def login(browser):
    browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
    browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
    browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))