from selenium import webdriver
from math import sin, log


URL = 'http://suninjuly.github.io/alert_accept.html'

driver = webdriver.Chrome('/home/anton/Загрузки/chromedriver')
driver.get(URL)

driver.find_element_by_css_selector('.btn').click()

driver.switch_to_alert().accept()


def calk(x):
    return str(log(abs(12*sin(int(x)))))


x = driver.find_element_by_id('input_value').text

answer = driver.find_element_by_id('answer')
answer.send_keys(calk(x))

driver.find_element_by_css_selector('.btn').click()

