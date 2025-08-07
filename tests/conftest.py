from datetime import datetime
from utils.driver import ChromeDriver, FirefoxDriver

import logging, os, pytest, pytest_html


@pytest.fixture
def driver():
    logger = logging.getLogger(__name__)

    if os.getenv("WEBDRIVER") == "firefox":
        logger.info("Using Firefox WebDriver")
        webdriver = FirefoxDriver().get_firefox_driver()
    else:
        logger.info("Using Chrome WebDriver")
        webdriver = ChromeDriver().get_chrome_driver()

    if os.getenv("HEADLESS"):
        logger.info("Running in headless mode")

    yield webdriver

    webdriver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.getenv("PYTHONPATH") + '/screenshots'
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_file = f"{screenshot_dir}/screenshot_{timestamp}.png"

            driver = item.funcargs['driver']
            driver.save_screenshot(screenshot_file)

            extras.append(pytest_html.extras.image(screenshot_file))

        report.extras = extras