import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = " https://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_inp = browser.find_element(By.ID, "input_value")
    x = int(x_inp.text)
    x = calc(x)
    inp = browser.find_element(By.TAG_NAME, "input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
    inp.send_keys(x)
    robot_check = browser.find_element(By.ID, "robotCheckbox")
    robot_check.click()
    rule_radio = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    rule_radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
