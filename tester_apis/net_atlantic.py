from selenium.webdriver.common.by import By

from utils.selenium_helper import go_to, send_keys_to_element, element


def net_atlantic_selenium_score(headline):
    go_to('http://emailsubjectlinegrader.com/')
    send_keys_to_element(By.ID, 'subjectTextId', headline)
    element(By.ID, 'goTopBtn').click()

    return element(By.CSS_SELECTOR, '#progress .progressbar-text').text
