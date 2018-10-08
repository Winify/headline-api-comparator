import time

from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from utils.open_browser import driver

current_time = int(round(time.time() * 1000))


def go_to(url):
    driver.get(url)


def delete_cookies():
    driver.delete_all_cookies()
    driver.refresh()
    pass


def element(by, selector):
    time.sleep(0.1)
    return WebDriverWait(driver, 10).until(visibility_of_element_located((by, selector)))


def wait_for_loading(by, selector):
    WebDriverWait(driver, 10).until(invisibility_of_element_located((by, selector)))
    time.sleep(1)


def send_keys_to_element(by, selector, text):
    elem = element(by, selector)
    elem.clear()
    elem.send_keys(text)
    return elem
