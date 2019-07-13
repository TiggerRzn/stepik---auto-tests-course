from selenium import webdriver
import os


URL = 'http://suninjuly.github.io/file_input.html'
URL2 = 'https://stepik.org/lesson/228249/step/8?after_pass_reset=true&unit=200781'

driver = webdriver.Chrome('/home/anton/PycharmProjects/web_driver/1/venv/1/chromedriver')
driver.get(URL)

# filling First name
driver.find_element_by_name('firstname').send_keys('Ivan')

# filling Last name
driver.find_element_by_name('lastname').send_keys('Ivanoff')

# filling E-mail
driver.find_element_by_name('email').send_keys('test@te.st')

driver.find_element_by_id('file').send_keys(os.path.abspath('/home/anton/Рабочий стол/1.txt'))

# click the button
driver.find_element_by_tag_name('button').click()

alert = driver.switch_to_alert()
alert_text = alert.text.split(': ')[-1]

print(alert_text)
alert.accept()





