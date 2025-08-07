from src.api import get_tmdb_api
from src.web import get_tmdb_page


def test_sorted_movie_popularity(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()

    tmdb_api = get_tmdb_api()
    movies_based_on_popularity_response = tmdb_api.get_movies_based_on_popularity(page=1)
    movies_based_on_popularity_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_popularity_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_tv_show_popularity(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    tv_show_based_on_popularity_response = tmdb_api.get_tv_show_based_on_popularity(page=1)
    tv_show_based_on_popularity_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = tv_show_based_on_popularity_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_movie_trend(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_trend_button()

    tmdb_api = get_tmdb_api()
    movies_based_on_trend_response = tmdb_api.get_movies_based_on_trend(page=1)
    movies_based_on_trend_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_trend_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_tv_show_trend(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_trend_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    tv_show_based_on_trend_response = tmdb_api.get_tv_show_based_on_trend(page=1)
    tv_show_based_on_trend_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = tv_show_based_on_trend_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_newest_movie(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_newest_button()

    tmdb_api = get_tmdb_api()
    get_newest_movie_response = tmdb_api.get_newest_movie(page=1)
    get_newest_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_newest_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_newest_tv_show(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_newest_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    get_newest_tv_show_response = tmdb_api.get_newest_tv_show(page=1)
    get_newest_tv_show_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = get_newest_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_top_rated_movie(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_top_rated_button()

    tmdb_api = get_tmdb_api()
    get_top_rated_movie_response = tmdb_api.get_top_rated_movie(page=1)
    get_top_rated_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_top_rated_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_top_rated_tv_show(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_top_rated_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    get_top_rated_tv_show_response = tmdb_api.get_top_rated_tv_show(page=1)
    get_top_rated_tv_show_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = get_top_rated_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_movie_with_1_additional_genre(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()

    tmdb_api = get_tmdb_api()
    movie_genre_list_response = tmdb_api.get_movie_genre_list()
    movie_genre_list_response.assert_response_status_code(200)

    random_genres = movie_genre_list_response.get_random_genres(1)
    tmdb_page.choose_genre(random_genres)

    filtered_movies_response = tmdb_api.get_filtered_movies(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_movies_response.assert_response_status_code(200)
    filtered_movies_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = filtered_movies_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_movie_with_2_additional_genre_then_remove_1_genre(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()

    tmdb_api = get_tmdb_api()
    movie_genre_list_response = tmdb_api.get_movie_genre_list()
    movie_genre_list_response.assert_response_status_code(200)

    random_genres = movie_genre_list_response.get_random_genres(2)
    tmdb_page.choose_genre(random_genres)

    filtered_movies_response = tmdb_api.get_filtered_movies(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_movies_response.assert_response_status_code(200)
    filtered_movies_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = filtered_movies_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

    # Remove two genre and verify the titles again
    tmdb_page.remove_random_genre(genres=random_genres, number_to_be_removed=1)

    filtered_movies_response = tmdb_api.get_filtered_movies(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_movies_response.assert_response_status_code(200)
    filtered_movies_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = filtered_movies_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_tv_show_with_1_additional_genre(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    tv_show_genre_list_response = tmdb_api.get_tv_show_genre_list()
    tv_show_genre_list_response.assert_response_status_code(200)

    random_genres = tv_show_genre_list_response.get_random_genres(1)
    tmdb_page.choose_genre(random_genres)

    filtered_tv_show_response = tmdb_api.get_filtered_tv_show(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_tv_show_response.assert_response_status_code(200)
    filtered_tv_show_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = filtered_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_tv_show_with_2_additional_genre_then_remove_1_genre(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()
    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_api = get_tmdb_api()
    tv_show_genre_list_response = tmdb_api.get_tv_show_genre_list()
    tv_show_genre_list_response.assert_response_status_code(200)

    random_genres = tv_show_genre_list_response.get_random_genres(2)
    tmdb_page.choose_genre(random_genres)

    filtered_tv_show_response = tmdb_api.get_filtered_tv_show(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_tv_show_response.assert_response_status_code(200)
    filtered_tv_show_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = filtered_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

    # Remove two genre and verify the titles again
    tmdb_page.remove_random_genre(genres=random_genres, number_to_be_removed=1)

    filtered_tv_show_response = tmdb_api.get_filtered_tv_show(
        sort_by="popularity",
        genres=random_genres
    )
    filtered_tv_show_response.assert_response_status_code(200)
    filtered_tv_show_response.assert_genres_in_response(random_genres)

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = filtered_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_search_movie_titles(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.fill_search_input("Demon Slayer")
    tmdb_page.verify_shown_titles_contains("Demon Slayer")

def test_search_tv_show_titles(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_type_dropdown()
    tmdb_page.click_dropdown_option("TV Shows")

    tmdb_page.fill_search_input("Demon Slayer")
    tmdb_page.verify_shown_titles_contains("Demon Slayer")

def test_discover_button(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_top_rated_button()

    tmdb_api = get_tmdb_api()
    get_top_rated_movie_response = tmdb_api.get_top_rated_movie(page=1)
    get_top_rated_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_top_rated_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

    tmdb_page.click_discover_button()

    movies_based_on_popularity_response = tmdb_api.get_movies_based_on_popularity(page=1)
    movies_based_on_popularity_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_popularity_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_pagination_on_second_page(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_trend_button()

    tmdb_api = get_tmdb_api()
    movies_based_on_trend_response = tmdb_api.get_movies_based_on_trend(page=1)
    movies_based_on_trend_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_trend_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

    # Click on the second page
    tmdb_page.click_page_number_button(2)

    movies_based_on_trend_response = tmdb_api.get_movies_based_on_trend(page=2)
    movies_based_on_trend_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_trend_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_pagination_on_list_shown_in_ui(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_newest_button()

    # Click on the fourth page
    tmdb_page.click_page_number_button(4)
    tmdb_page.verify_page_number_button_shown(4)

    # Click on the fifth page
    tmdb_page.click_page_number_button(5)
    tmdb_page.verify_page_number_button_shown(5)

    # Click on the sixth page
    tmdb_page.click_page_number_button(6)
    tmdb_page.verify_page_number_button_shown(6)

def test_navigation_of_pagination_page(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_top_rated_button()

    # Click on the fourth page
    tmdb_page.click_page_number_button(4)
    tmdb_page.click_page_next_button()

    tmdb_api = get_tmdb_api()
    get_top_rated_movie_response = tmdb_api.get_top_rated_movie(page=5)
    get_top_rated_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_top_rated_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

    tmdb_page.click_page_previous_button()

    get_top_rated_movie_response = tmdb_api.get_top_rated_movie(page=4)
    get_top_rated_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_top_rated_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_pagination_on_last_page(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    # Click on the fourth page
    last_page_number = tmdb_page.get_last_page_number()
    tmdb_page.click_page_number_button(last_page_number)

    tmdb_api = get_tmdb_api()
    get_newest_movie_response = tmdb_api.get_newest_movie(page=last_page_number)
    get_newest_movie_response.assert_response_status_code(200)

    # Verify whether the titles that shown in UI based on the API response
    movie_names = get_newest_movie_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)