from utils.driver import ChromeDriver, FirefoxDriver

import os, pytest


@pytest.fixture
def driver():
    if os.getenv("WEBDRIVER") == "firefox":
        webdriver = FirefoxDriver().get_firefox_driver()
    webdriver = ChromeDriver().get_chrome_driver()

    yield webdriver

    webdriver.quit()