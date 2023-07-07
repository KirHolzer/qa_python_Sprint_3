from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls, TestData

class TestLogin:
    def test_login_from_main_page(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url

    def test_login_from_account_page(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url

    def test_login_from_registration_page(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.LINK_TO_REGISTRATION_PAGE_FRON_ACCOUNT).click()
        browser.find_element(*TestLocators.LOGIN_BUTTON_REGISTER).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url

    def test_login_from_recovery_page(self, browser):
        browser.get(TestUrls.forgot_password_url)
        browser.find_element(*TestLocators.LOGIN_BUTTON_RECOVERY).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert browser.current_url == TestUrls.main_url








