from locators import TestLocators
from data import TestUrls
from helpers import login

class TestLogin:

    def test_login_from_main_page(self, browser):
        """
            Проверяет вход в аккаунт с главной страницы.
        """
        browser.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON).click()
        login(browser)
        assert browser.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_account_page(self, browser):
        """
            Проверяет вход в аккаунт с личного кабинета.
        """
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        login(browser)
        assert browser.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_registration_page(self, browser):
        """
            Проверяет вход в аккаунт со страницы регистрации.
        """
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        browser.find_element(*TestLocators.LINK_TO_REGISTRATION_PAGE_FRON_ACCOUNT).click()
        browser.find_element(*TestLocators.LOGIN_BUTTON_REGISTRATION).click()
        login(browser)
        assert browser.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

    def test_login_from_recovery_page(self, browser):
        """
            Проверяет вход в аккаунт со страницы востановления пароля.
        """
        browser.get(TestUrls.forgot_password_url)
        browser.find_element(*TestLocators.LOGIN_BUTTON_RECOVERY).click()
        login(browser)
        assert browser.find_element(*TestLocators.MAKE_ORDER_BUTTON).text == "Оформить заказ"

