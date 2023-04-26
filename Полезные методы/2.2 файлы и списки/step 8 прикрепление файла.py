from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name1 = browser.find_element(By.NAME , "firstname")
    name1.send_keys("Anton")
    name2 = browser.find_element(By.NAME, "lastname")
    name2.send_keys("Tagiev")
    email=browser.find_element(By.NAME,"email")
    email.send_keys("abc@gmail.com")
    file_send=browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
    file_send.send_keys(file_path)
    subm=browser.find_element(By.TAG_NAME, 'button')
    subm.click()
finally:
    time.sleep(10)
    browser.quit()