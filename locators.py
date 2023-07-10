from selenium.webdriver.common.by import By

class TestLocators:

    # Локаторы для проверки регистрации
    NAME_INPUT_REGISTRATION = By.XPATH, ".//fieldset[1]//input"
    EMAIL_INPUT_REGISTRATION = By.XPATH, ".//fieldset[2]//input"
    PASSWORD_INPUT_REGISTRATION = By.NAME, "Пароль"
    REGISTRATION_BUTTON = By.TAG_NAME, "button"
    LOGIN_BUTTON_REGISTRATION = By.XPATH, ".//a[text()='Войти']"
    PASSWORD_INPUT_ERROR_REGISTRATION = By.XPATH, ".//p[text()='Некорректный пароль']"
    LINK_TO_REGISTRATION_PAGE_FRON_ACCOUNT = By.XPATH, ".//a[@class = 'Auth_link__1fOlj']"

    # Локаторы для проверки авторизации
    LOGIN_ACCOUNT_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    EMAIL_INPUT_LOGIN = By.XPATH, ".//fieldset[1]//input"
    PASSWORD_INPUT_LOGIN = By.NAME, "Пароль"
    LOGIN_BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"
    LOGIN_BANNER = By.XPATH, ".//h2[text()='Вход']"
    LOGIN_BUTTON_RECOVERY = By.XPATH, ".//a[text()='Войти']"
    HEADING_ON_LOG_IN_PAGE = By.XPATH, ".//h2[text() ='Вход']"

    # Локатор для проверки деавторизации
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ACCOUNT_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"

    # Локаторы для проверки конструктора
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']"      # Локатор кнопки конструктора в хеддере
    LOGO_MAIN = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"       # Локатор лого  в хеддере

    BUNS_BUTTON = By.XPATH, ".//span[text()='Булки']"                # Локатор булки в навигации конструктора
    SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']"              # Локатор соусов в навигации конструктора
    FILLER_BUTTON = By.XPATH, ".//span[text()='Начинки']"            # Локатор начинки в навигации конструктора

    BUNS_BANNER = By.XPATH, ".//h2[text()='Булки']"                  # Локатор булки в скролле h2 конструктора
    SAUCES_BANNER = By.XPATH, ".//h2[text()='Соусы']"                # Локатор соусов в скролле h2 конструктора
    TOPPINGS_BANNER = By.XPATH, ".//h2[text()='Начинки']"            # Локатор начинки в скролле h2 конструктора

    CURRENT_TAB = By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]" # Локатор выброанной навигации конструктора
    MAKE_BURGER_BANNER = By.XPATH, ".//h1[text()='Соберите бургер']"    # Локатор 'Соберите бургер' на главной странице
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text()='Оформить заказ']"  # Локатор кнопки 'Оформить заказ' на главной странице
