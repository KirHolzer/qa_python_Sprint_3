from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls
from data import TestData

class TestLogOut:

    def test_logout_from_account_page(self, browser):
        browser.get(TestUrls.main_url)
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.EMAIL_INPUT_LOGIN).send_keys(TestData.valid_email_for_login)
        browser.find_element(*TestLocators.PASSWORD_INPUT_LOGIN).send_keys(TestData.valid_password_for_login)
        browser.find_element(*TestLocators.LOGIN_BUTTON_LOGIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert browser.current_url == TestUrls.login_url
