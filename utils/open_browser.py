from selenium import webdriver

selenium_hub = 'http://192.168.99.100:4444'

# driver = webdriver.Remote(selenium_hub + "/wd/hub", DesiredCapabilities.CHROME)
driver = webdriver.Chrome()

driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
