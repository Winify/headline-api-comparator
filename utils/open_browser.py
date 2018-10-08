from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

selenium_hub = 'http://192.168.99.100:4444'

driver = webdriver.Remote(selenium_hub + "/wd/hub", DesiredCapabilities.CHROME)

driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
