from selenium import webdriver
from math import sin, log
URL = 'http://SunInJuly.github.io/execute_script.html'

driver = webdriver.Chrome('/home/anton/PycharmProjects/web_driver/1/venv/1/chromedriver')
driver.get(URL)


def calc(x):
    return str(log(abs(12*sin(int(x)))))


result = calc(driver.find_element_by_id('input_value').text)
driver.find_element_by_id('answer').send_keys(result)

button = driver.find_element_by_tag_name('button')
driver.execute_script("return arguments[0].scrollIntoView(true);", button)

driver.find_element_by_id('robotCheckbox').click()
driver.find_element_by_id('robotsRule').click()

button.click()