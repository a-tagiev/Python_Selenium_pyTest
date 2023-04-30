import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#idk
class Test(unittest.TestCase):
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    required_fields = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    for i in required_fields:
        if i.get_attribute(By.CLASS_NAME)==".first" or i.get_attribute(By.CLASS_NAME)==".second":
            i.send_keys("мяу")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    #проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    def test1(self,welcome_text):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

