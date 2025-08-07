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
    page_number_button = "//a[@aria-label='Page {page_number}']"
    page_number_button_elements = "//ul/li/a[@role='button']"
    page_next_button = "//a[@aria-label='Next page']"
    page_previous_button = "//a[@aria-label='Previous page']"


class TmdbPage(PageBase):
    def open(self):
        self.logger.info(f"open TMDB page")
        self.driver.get("https://tmdb-discover.surge.sh/")

        while self.driver.execute_script("return document.readyState;") != "complete":
            time.sleep(1)

        self.driver.maximize_window()
        
    def click_popular_button(self):
        self.logger.info("Clicking on popular button")

        popular_button = self.get_visible_element(TmdbLocators.popular_button)
        popular_button.click()

    def verify_shown_titles(self, titles):
        self.logger.info("Verifying shown titles")

        # Wait for elements to load
        time.sleep(1.5)

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
        self.logger.info("Clicking on type dropdown")

        type_dropdown = self.get_all_visible_elements(TmdbLocators.dropdown)
        type_dropdown[0].click()

    def click_dropdown_option(self, value):
        self.logger.info(f"Clicking on dropdown option with value: {value}")

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
        self.logger.info("Clicking on trend button")

        trend_button = self.get_visible_element(TmdbLocators.trend_button)
        trend_button.click()

    def click_newest_button(self):
        self.logger.info("Clicking on newest button")

        newest_button = self.get_visible_element(TmdbLocators.newest_button)
        newest_button.click()
    
    def click_top_rated_button(self):
        self.logger.info("Clicking on top rated button")

        top_rated_button = self.get_visible_element(TmdbLocators.top_rated_button)
        top_rated_button.click()

    def fill_search_input(self, title):
        self.logger.info(f"Filling search input with title: {title}")

        search_input = self.get_visible_element(TmdbLocators.search_input)
        search_input.clear()
        search_input.send_keys(title)

        # Wait for search results to load
        time.sleep(2)

    def verify_shown_titles_contains(self, title):
        self.logger.info(f"Verifying shown titles that contains {title}")

        text_elements = self.get_all_visible_elements(TmdbLocators.movie_and_tv_title_text)

        for text_element in text_elements:
            self.logger.info(f"Assert {title} in {text_element.text}")

            assert title in text_element.text, f"'{title}' not found in {text_element.text}"

    def click_discover_button(self):
        self.logger.info("Clicking on discover button")

        discover_button = self.get_visible_element(TmdbLocators.discover_button)
        discover_button.click()

    def click_page_number_button(self, page_number):
        self.logger.info(f"Clicking on page number button: {page_number}")

        page_button = self.get_visible_element(TmdbLocators.page_number_button.format(page_number=page_number))
        page_button.click()

    def verify_page_number_button_shown(self, page_number):
        self.logger.info("Verifying page number button shown")

        expected_list = []
        if page_number == 1:
            expected_list = [1, 2, 3, "..."]
        elif page_number <= 5:
            for number in range(1, page_number+2, 1):
                expected_list.append(number)
            expected_list.append("...")
        else:
            expected_list = [1, 2, 3,"...", page_number-1, page_number, page_number+1, "..."]

        self.logger.info(f"Expected list: {expected_list} page number button that will be shown")
        page_number_button_elements = self.get_all_visible_elements(TmdbLocators.page_number_button_elements)

        for i in range(len(expected_list)):
            self.logger.info(f"Assert {expected_list[i]} with {page_number_button_elements[i+1].text}")

            assert str(expected_list[i]) == page_number_button_elements[i+1].text, (
                f"Actual result: {page_number_button_elements[i+1].text}, "
                f"is not equal to expected result: {expected_list[i]}"
            )

    def click_page_next_button(self):
        self.logger.info("Clicking on page next button")

        page_next_button = self.get_visible_element(TmdbLocators.page_next_button)
        page_next_button.click()
    
    def click_page_previous_button(self):
        self.logger.info("Clicking on page previous button")

        page_previous_button = self.get_visible_element(TmdbLocators.page_previous_button)
        page_previous_button.click()
    
    def get_last_page_number(self):
        page_number_button_elements = self.get_all_visible_elements(TmdbLocators.page_number_button_elements)
        last_page_number = page_number_button_elements[-1].text

        self.logger.info(f"Last page number: {last_page_number}")

        return page_number_button_elements[-2].text