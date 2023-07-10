from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import TestConstructorNavigationText

class TestConstructorNavigation:

    def test_const_go_to_toppings(self, browser):
        """
            Проверяет переход к разделу "Топпинги" в конструкторе.
        """
        browser.find_element(*TestLocators.FILLER_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.TOPPINGS_BANNER))
        current_navigation_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestConstructorNavigationText.filler_navigation_text == current_navigation_text

    def test_const_go_to_sauces(self, browser):
        """
            Проверяет переход к разделу "Соусы" в конструкторе.
        """
        browser.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_BANNER))
        current_navigation_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestConstructorNavigationText.sauces_navigation_text == current_navigation_text

    def test_const_go_to_buns(self, browser):
        """
            Проверяет переход к разделу "Булки" в конструкторе.
        """
        browser.find_element(*TestLocators.FILLER_BUTTON).click()
        browser.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(browser, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS_BANNER))
        current_navigation_text = browser.find_element(*TestLocators.CURRENT_TAB).text
        assert TestConstructorNavigationText.buns_navigation_text == current_navigation_text