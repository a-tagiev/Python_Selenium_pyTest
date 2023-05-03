from selenium import webdriver
from selenium.webdriver.common.by import By


def m(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполнение обязательных полей
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("name")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("last name")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        email.send_keys("mail@gmail.com")
        # Отправка формы
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_1():
    link = "http://suninjuly.github.io/registration1.html"
    welcome_text = m(link)
    assert "Congratulations! You have successfully registered!", welcome_text


def test_2():
    link = "http://suninjuly.github.io/registration2.html"
    welcome_text = m(link)
    assert "Congratulations! You have successfully registered!", welcome_text
