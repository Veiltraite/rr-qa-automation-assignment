from selenium import webdriver

class ChromeDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_chrome_driver(self):
        return self.driver


class FirefoxDriver:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_firefox_driver(self):
        return self.driver