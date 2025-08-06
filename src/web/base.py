from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import logging


class PageBase():
    def __init__(self, driver):
        self.logger = logging.getLogger(__name__)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, *, expected_condition, locator):
        if locator[0] == "/" or locator[1] == "/":
            by_locator = By.XPATH
        else:
            by_locator = By.ID

        return self.wait.until(
            expected_condition((by_locator, locator)),
            message=f"element with locator '{locator}' is not visible",
        )

    def get_visible_element(self, locator):
        expected_condition = expected_conditions.visibility_of_element_located

        return self.get_element(
            expected_condition=expected_condition, locator=locator
        )

    def get_all_visible_elements(self, locator):
        expected_condition = expected_conditions.visibility_of_all_elements_located

        return self.get_element(
            expected_condition=expected_condition, locator=locator
        )