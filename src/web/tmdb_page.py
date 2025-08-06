from src.web.base import PageBase


class TmdbLocators:
    popular_button = "//a[@href='/popular']"


class TmdbPage(PageBase):
    def open(self):
        self.logger.info(f"open TMDB page")
        self.driver.get("https://tmdb-discover.surge.sh/")

        while self.driver.execute_script("return document.readyState;") != "complete":
            time.sleep(1)
        
    def verify_popular_button_visible(self):
        self.logger.info("Verifying that the popular button is visible")

        popular_button = self.get_visible_element(TmdbLocators.popular_button)
        assert popular_button.is_displayed(), "Popular button is not visible on the TMDB page"