from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from helpers import login

class TestLogOut:

    def test_logout_from_account_page(self, browser):

        browser.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        login(browser)
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*TestLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

