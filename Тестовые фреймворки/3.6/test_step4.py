from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_authorization(browser):
    '''
    Проверка того, что мы можем залогиниться на сайте
    '''
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys("email")
    browser.find_element(By.ID, "id_login_password").send_keys("pwd")
    browser.find_element(By.XPATH, '//button[text()="Log in"]').click()
