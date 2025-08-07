from src.web.base import PageBase

import random, time


class TmdbLocators:
    popular_button = "//a[@href='/popular']"
    movie_and_tv_title_text = "//p[contains(@class, 'py-1')]"
    dropdown = "//div[contains(@class,'css-2b097c-container')]//div[contains(@class,'css-1wy0on6')]"
    dropdown_option = "//div[contains(@id,'react-select') and text()='{value}']"
    remove_genre_button = "//div[contains(@class,'css-1rhbuit-multiValue')]/div[text()='{value}']/following-sibling::div"
    trend_button = "//a[@href='/trend']"
    newest_button = "//a[@href='/new']"
    top_rated_button = "//a[@href='/top']"
    search_input = "//input[@name='search']"
    discover_button = "//p[text()='Discover']"


class TmdbPage(PageBase):
    def open(self):
        self.logger.info(f"open TMDB page")
        self.driver.get("https://tmdb-discover.surge.sh/")

        while self.driver.execute_script("return document.readyState;") != "complete":
            time.sleep(1)

        self.driver.maximize_window()
        
    def click_popular_button(self):
        self.logger.info("Clicking on the popular button")

        popular_button = self.get_visible_element(TmdbLocators.popular_button)
        popular_button.click()

    def verify_shown_titles(self, titles):
        self.logger.info("Verifying the shown titles")

        movie_and_tv_title_text = self.get_all_visible_elements(TmdbLocators.movie_and_tv_title_text)
        
        index = 0
        for title in titles:
            text = movie_and_tv_title_text[index].text
            self.logger.info(
                f"Assert title in UI: '{text}' with '{title}'"
            )

            assert text == title, (
                f"Actual result: {text}, "
                f"is not equal to expected result: {title}"
            )

            index += 1

    def click_type_dropdown(self):
        self.logger.info("Clicking on the type dropdown")

        type_dropdown = self.get_all_visible_elements(TmdbLocators.dropdown)
        type_dropdown[0].click()

    def click_dropdown_option(self, value):
        self.logger.info(f"Clicking on the dropdown option with value: {value}")

        dropdown_option = self.get_visible_element(
            TmdbLocators.dropdown_option.format(value=value)
        )

        dropdown_option.click()

    def choose_genre(self, genres):
        self.logger.info(f"Choosing genres: {genres}")

        for genre in genres:
            type_dropdown = self.get_all_visible_elements(TmdbLocators.dropdown)
            type_dropdown[1].click()

            dropdown_option = self.get_visible_element(
                TmdbLocators.dropdown_option.format(value=genre["name"])
            )

            dropdown_option.click()
            
            self.get_all_visible_elements(TmdbLocators.movie_and_tv_title_text)

    def remove_random_genre(self, genres, number_to_be_removed=1):
        random_genres = random.sample(genres, number_to_be_removed)

        for genre in random_genres:
            self.logger.info(f"Removing genre: {genre}")
            removed_genre = genres.pop(genres.index(genre))

            remove_genre_button = self.get_visible_element(
                TmdbLocators.remove_genre_button.format(value=removed_genre["name"])
            )

            remove_genre_button.click()

            self.get_all_visible_elements(TmdbLocators.movie_and_tv_title_text)

    def click_trend_button(self):
        self.logger.info("Clicking on the trend button")

        trend_button = self.get_visible_element(TmdbLocators.trend_button)
        trend_button.click()

    def click_newest_button(self):
        self.logger.info("Clicking on the newest button")

        newest_button = self.get_visible_element(TmdbLocators.newest_button)
        newest_button.click()
    
    def click_top_rated_button(self):
        self.logger.info("Clicking on the top rated button")

        top_rated_button = self.get_visible_element(TmdbLocators.top_rated_button)
        top_rated_button.click()

    def fill_search_input(self, title):
        self.logger.info(f"Filling search input with title: {title}")

        search_input = self.get_visible_element(TmdbLocators.search_input)
        search_input.clear()
        search_input.send_keys(title)

        # Wait for search results to load
        time.sleep(3)

    def verify_shown_titles_contains(self, title):
        self.logger.info(f"Verifying the shown titles contains {title}")

        text_elements = self.get_all_visible_elements(TmdbLocators.movie_and_tv_title_text)

        for text_element in text_elements:
            self.logger.info(f"Assert {title} in {text_element.text}")

            assert title in text_element.text, f"'{title}' not found in {text_element.text}"

    def click_discover_button(self):
        self.logger.info("Clicking on the discover button")

        discover_button = self.get_visible_element(TmdbLocators.discover_button)
        discover_button.click()