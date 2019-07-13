from selenium import webdriver
from math import sin, log


URL = 'http://suninjuly.github.io/redirect_accept.html'

driver = webdriver.Chrome('/home/anton/Загрузки/chromedriver')
driver.get(URL)

driver.find_element_by_css_selector('.btn').click()

new_window = driver.window_handles[1]

driver.switch_to_window(new_window)

x = driver.find_element_by_css_selector('#input_value').text
print(x)


def calculate(a):
    return str(log(abs(12*sin(int(a)))))


# find element by id 'answer'
driver.find_element_by_css_selector('#answer').send_keys(calculate(x))
# find element by class name 'btn'
driver.find_element_by_css_selector('.btn').click()

# alert text, split numbers
number = driver.switch_to_alert().text.split(': ')[-1]
print(number)

# alert acception
driver.switch_to_alert().accept()


