from selenium import webdriver
from selenium.webdriver.support.select import Select


URL = 'http://suninjuly.github.io/selects2.html'

driver = webdriver.Chrome('/home/anton/PycharmProjects/web_driver/1/venv/1/chromedriver')
driver.get(URL)


def calc(x, y):
    return str(int(x) + int(y))


x = driver.find_element_by_id('num1').text
y = driver.find_element_by_id('num2').text

select = Select(driver.find_element_by_class_name('custom-select'))

select.select_by_value(str(calc(x, y)))

driver.find_element_by_tag_name('button').click()
