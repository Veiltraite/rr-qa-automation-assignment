from utils.driver import ChromeDriver, FirefoxDriver

import os, pytest

@pytest.fixture
def driver():
    if os.getenv("WEBDRIVER") == "firefox":
        return FirefoxDriver().get_firefox_driver()

    return ChromeDriver().get_chrome_driver()