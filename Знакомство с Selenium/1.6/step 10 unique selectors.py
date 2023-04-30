from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input")
    input1.send_keys("-")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input")
    input2.send_keys("-")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input")
    input3.send_keys("test@test.com")

    # Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
