from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID , "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    ans = int(x) + int(y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(ans))
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")

    button.click()

finally:
    time.sleep(10)
    browser.quit()
