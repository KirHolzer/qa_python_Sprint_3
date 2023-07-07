from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestUrls, TestData



class TestRegistration:
    def test_registration_success(self, browser):
        email, name = TestData.email()
        browser.get(TestUrls.register_url)
        browser.find_element(*TestLocators.NAME_INPUT_REGISTER).send_keys(name)
        browser.find_element(*TestLocators.EMAIL_INPUT_REGISTER).send_keys(email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_REGISTER).send_keys(TestData.generate_correct_password_six_symbols())
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN))
        assert browser.current_url != TestUrls.register_url, 'При валидных данных не выполнен переход к логину!'

    def test_registration_pass_error(self, browser):
        email, name = TestData.email()
        browser.get(TestUrls.register_url)
        browser.find_element(*TestLocators.NAME_INPUT_REGISTER).send_keys(name)
        browser.find_element(*TestLocators.EMAIL_INPUT_REGISTER).send_keys(email)
        browser.find_element(*TestLocators.PASSWORD_INPUT_REGISTER).send_keys(TestData.generate_uncorrect_password_less_then_six_symbols())
        browser.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(TestLocators.PASSWORD_INPUT_ERROR_REGISTER))
        browser.find_element(*TestLocators.PASSWORD_INPUT_ERROR_REGISTER)
        expected_text = "Некорректный пароль"
        assert browser.find_element(*TestLocators.PASSWORD_INPUT_ERROR_REGISTER).text == expected_text





