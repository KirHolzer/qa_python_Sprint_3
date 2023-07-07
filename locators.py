from selenium.webdriver.common.by import By

class TestLocators:


    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"
    LOGO_MAIN = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    ACCOUNT_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    LOGIN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"
    MAKE_BURGER_BANNER = By.XPATH, ".//h1[text()='Соберите бургер']"
    BUNS_BUTTON = By.XPATH, ".//span[text()='Булки']"
    BUNS_BANNER = By.XPATH, ".//h2[text()='Булки']"
    SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']"
    SAUCES_BANNER = By.XPATH, ".//h2[text()='Соусы']"
    TOPPINGS_BUTTON = By.XPATH, ".//span[text()='Начинки']"
    TOPPINGS_BANNER = By.XPATH, ".//h2[text()='Начинки']"
    CURRENT_TAB = By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"

    NAME_INPUT_REGISTER = By.XPATH, ".//fieldset[1]//input"
    EMAIL_INPUT_REGISTER = By.XPATH, ".//fieldset[2]//input"
    PASSWORD_INPUT_REGISTER = By.NAME, "Пароль"
    REGISTRATION_BUTTON = By.TAG_NAME, "button"
    PASSWORD_INPUT_ERROR_REGISTER = By.XPATH, ".//p[text()='Некорректный пароль']"
    LOGIN_BUTTON_REGISTER = By.XPATH, ".//a[text()='Войти']"

    EMAIL_INPUT_LOGIN = By.XPATH, ".//fieldset[1]//input"
    PASSWORD_INPUT_LOGIN = By.NAME, "Пароль"
    LOGIN_BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"
    LOGIN_BANNER = By.XPATH, ".//h2[text()='Вход']"

    LOGIN_BUTTON_RECOVERY = By.XPATH, ".//a[text()='Войти']"

    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"

    LINK_TO_REGISTRATION_PAGE_FRON_ACCOUNT = By.XPATH, ".//a[@class = 'Auth_link__1fOlj']"

print(TestLocators.EMAIL_INPUT_REGISTER)