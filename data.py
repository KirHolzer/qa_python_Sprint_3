from faker import Faker
fake = Faker()

# Функция для генерации случайного электронного адреса имени
class TestData:
    def email():
        name = fake.first_name()
        surname = fake.last_name()
        domain = "ya.ru"
        email = f"{name.lower()}_{surname.lower()}@{domain}"
        return email, name
    # Функции для генерации пароля
    def generate_correct_password_six_symbols(min_length=6):
        fake = Faker()
        password = fake.password(length=max(min_length, 6))
        return password
    def generate_correct_password_more_then_six_symbols(min_length=6):
        fake = Faker()
        password_length = fake.random_int(min=min_length,max=min_length + 10)  # Генерируем случайную длину пароля от min_length до min_length+10
        password = fake.password(length=password_length)
        return password
    def generate_uncorrect_password_less_then_six_symbols(max_length=5):
        fake = Faker()
        password_length = fake.random_int(min=4, max=max_length)
        password = fake.password(length=password_length)
        return password

    valid_email_for_login = 'kirill.holzer@yandex.ru'
    valid_password_for_login = 'qwerty'


class TestUrls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    register_url = 'https://stellarburgers.nomoreparties.site/register'
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'


#email = email()
#correct_password_six_symbols = generate_correct_password_six_symbols()
#correct_password_more_then_six_symbols = generate_correct_password_more_then_six_symbols()
#uncorrect_password_less_then_six_symbols = generate_uncorrect_password_less_then_six_symbols()

print(TestData.email())
print(TestData.generate_correct_password_six_symbols())
print(TestData.generate_correct_password_more_then_six_symbols())
print(TestData.generate_uncorrect_password_less_then_six_symbols())

