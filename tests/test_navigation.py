from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls

class TestNavigation:

    def test_go_to_account_from_main_page(self, browser):
        """
            Проверяет переход с главной страницы в личный кабинет.
        """
        browser.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert browser.current_url == TestUrls.login_url

    def test_go_to_constructor_from_account_on_button(self, browser):
        """
            Проверяет переход из личного кабинета на главную страницу через кнопку конструктора в хеддере.
        """
        browser.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url

    def test_go_to_constructor_from_account_on_logo(self, browser):
        """
            Проверяет переход из личного кабинета на главную страницу через клик по логотипу в хеддере.
        """
        browser.find_element(*TestLocators.LOGO_MAIN).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_BURGER_BANNER))
        assert browser.current_url == TestUrls.main_url

