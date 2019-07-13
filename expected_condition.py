from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import sin, log


browser = webdriver.Chrome('/home/anton/Загрузки/chromedriver')
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
     )
button = browser.find_element_by_css_selector('#book')
button.click()

x = browser.find_element_by_css_selector('#input_value').text
print(x)


def calculate(a):
    return str(log(abs(12*sin(int(a)))))


# find element by id 'answer'
browser.find_element_by_css_selector('#answer').send_keys(calculate(x))
# find element by class name 'btn'
browser.find_element_by_css_selector('#solve').click()


# message = browser.find_element_by_id("check_message")
#
# assert "успешно" in message.text

