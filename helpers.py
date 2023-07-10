from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators
from data import TestData, TestUrls

def login(browser):
    browser.find_element(*AuthLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
    browser.find_element(*AuthLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
    browser.find_element(*AuthLocators.LOGIN_BUTTON_LOGIN).click()
    WebDriverWait(browser, 3).until(
        expected_conditions.visibility_of_element_located(AuthLocators.MAKE_ORDER_BUTTON))

def registration(browser, name, email, password):
    browser.get(TestUrls.register_url)
    browser.find_element(*AuthLocators.NAME_INPUT_REGISTRATION).send_keys(name)
    browser.find_element(*AuthLocators.EMAIL_INPUT_REGISTRATION).send_keys(email)
    browser.find_element(*AuthLocators.PASSWORD_INPUT_REGISTRATION).send_keys(password)
    browser.find_element(*AuthLocators.REGISTRATION_BUTTON).click()
