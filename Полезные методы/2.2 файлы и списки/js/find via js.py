from selenium import webdriver

#Вместо встроенных find_element_by... можно использовать вот такую конструкцию:
element = browser.execute_script('document.getElementsByName("name")')

#Так же есть конструкции:
#getElementById
#getElementsByTagName
#getElementsByClassName