import time

from selenium.webdriver.common.by import By

from utils.selenium_helper import element, send_keys_to_element, current_time, go_to


def select_last_option(selector):
    options = element(By.CSS_SELECTOR, selector).find_elements_by_tag_name('option')
    options[len(options) - 1].click()


def send_dummy_credentials():
    send_keys_to_element(By.NAME, 'name', 'Selenium {}'.format(current_time))
    send_keys_to_element(By.NAME, 'email', 'selenium{}@automation.com'.format(current_time))
    send_keys_to_element(By.NAME, 'company', 'Selenium Co.')
    send_keys_to_element(By.NAME, 'website', 'automation.com')
    time.sleep(0.5)

    select_last_option('select[name=description]')
    select_last_option('select[name=teamsize]')
    select_last_option('select[name=usecase]')

    element(By.ID, 'aj-lead-form').submit()


def co_schedule_selenium_score(first_query, headline):
    go_to('https://coschedule.com/headline-analyzer')
    send_keys_to_element(By.ID, 'aj-analyze-input', headline).submit()

    if first_query:
        send_dummy_credentials()

    return element(By.CSS_SELECTOR, '.circle1 + div.inset div.score').text
