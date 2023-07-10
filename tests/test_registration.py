from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import AuthLocators
from data import TestData
from helpers import registration



class TestRegistration:

    def test_registration_success_by_password_six_symbols(self, browser):
        """
            Проверяет успешную регистрацию пользователя с паролем из 6 символов .
        """
        email, name = TestData.email()
        password = TestData.generate_correct_password_six_symbols()
        registration(browser, name, email,password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*AuthLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

    def test_registration_success_by_password_more_then_six_symbols(self, browser):
        """
            Проверяет успешную регистрацию пользователя с паролем более 6 символов (до 10 включительно).
        """
        email, name = TestData.email()
        password = TestData.generate_correct_password_more_then_six_symbols()
        registration(browser, name, email, password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.LOGIN_BUTTON_LOGIN))
        assert browser.find_element(*AuthLocators.HEADING_ON_LOG_IN_PAGE).text == "Вход"

    def test_registration_failed_error(self, browser):
        """
            Проверяет сообщение об ошибке "Некорректный пароль", при пароле меньше 6 символов при регистрации пользователя.
        """
        email, name = TestData.email()
        password = TestData.generate_uncorrect_password_less_then_six_symbols()
        registration(browser, name, email, password)
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(AuthLocators.PASSWORD_INPUT_ERROR_REGISTRATION))
        expected_text = "Некорректный пароль"
        assert browser.find_element(*AuthLocators.PASSWORD_INPUT_ERROR_REGISTRATION).text == expected_text