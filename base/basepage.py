from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, location, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(*location))
        return element

    def find_eles(self, location, timeout=10):
        # element = self.driver.find_element(*location)
        element = WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(*location))
        return element

    def click_func(self, location, timeout=10):
        self.find_ele(location, timeout).click()

    def input_func(self, location, text, timeout=10):
        ele = self.find_ele(location, timeout)
        ele.clear()
        ele.send_keys(text)
