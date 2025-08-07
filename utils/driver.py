from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import os

class ChromeDriver:
    def __init__(self):
        options = ChromeOptions()

        if os.getenv("HEADLESS"):
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)

    def get_chrome_driver(self):
        return self.driver


class FirefoxDriver:
    def __init__(self):
        options = FirefoxOptions()

        if os.getenv("HEADLESS"):
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Firefox(options=options)

    def get_firefox_driver(self):
        return self.driver