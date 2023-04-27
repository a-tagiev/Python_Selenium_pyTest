import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(By.ID, "input_value").text)
    x = calc(x)
    inp = browser.find_element(By.TAG_NAME, "input")
    inp.send_keys(x)
    subm = browser.find_element(By.TAG_NAME, 'button')
    subm.click()
finally:
    time.sleep(5)
    browser.quit()
