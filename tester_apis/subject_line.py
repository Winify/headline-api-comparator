from selenium.webdriver.common.by import By

from utils.selenium_helper import go_to, delete_cookies, send_keys_to_element, element, wait_for_loading


def subject_line_selenium_score(headline):
    go_to('http://www.subjectline.com/')
    delete_cookies()

    send_keys_to_element(By.ID, 'txtSubjectLine', headline).submit()
    wait_for_loading(By.ID, 'loading')

    return element(By.ID, 'slScoreAnim').text
