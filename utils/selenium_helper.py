import time

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utils.open_browser import driver

current_time = int(round(time.time() * 1000))


def go_to(url):
    driver.get(url)


def element(by, selector):
    time.sleep(0.1)
    return WebDriverWait(driver, 10).until(visibility_of_element_located((by, selector)))


def send_keys_to_element(by, selector, text):
    elem = element(by, selector)
    elem.clear()
    elem.send_keys(text)
    return elem
