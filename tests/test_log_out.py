from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators
from helpers import login

class TestLogOut:

    def test_logout_from_account_page(self, browser):
        """
            Проверяет выход из аккаунта из личного кабинета.
        """
        browser.find_element(*AuthLocators.LOGIN_ACCOUNT_BUTTON).click()
        login(browser)
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(AuthLocators.MAKE_ORDER_BUTTON))
        browser.find_element(*AuthLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*AuthLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

