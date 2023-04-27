import math
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn = WebDriverWait(browser, 13).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    x = int(browser.find_element(By.ID, "input_value").text)
    x = calc(x)
    inp = browser.find_element(By.TAG_NAME, 'input')
    inp.send_keys(x)
    subm = browser.find_element(By.ID, "solve")
    subm.click()
finally:
    time.sleep(5)
    browser.quit()
