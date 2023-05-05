import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

ans = []
'''
Чего не хватает в коде и что желательно доработать

проверка на отсутствие кнопки решить снова
'''


@pytest.mark.parametrize('steps', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_authorization(browser, steps):
    f = open('ans.txt', 'w')
    link = f"https://stepik.org/lesson/{steps}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    browser.find_element(By.ID, "id_login_email").send_keys("email@gmail.com")
    browser.find_element(By.ID, "id_login_password").send_keys("pwd")
    browser.find_element(By.XPATH, '//button[text()="Log in"]').click()
    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    textar = browser.find_element(By.CSS_SELECTOR, "textarea")
    textar.send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    ifcor_check = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
    ifcor = ifcor_check.text
    f.write(ifcor)
    assert ifcor == "Correct!", f"expected 'Correct!', got {ifcor}"

    ans.append(ifcor)
    f.close()


print(ans)
