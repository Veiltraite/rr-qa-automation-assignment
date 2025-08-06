from src.api import get_tmdb_api
from src.web import get_tmdb_page


def test_sorted_movie_popularity(driver):
    tmdb_page = get_tmdb_page(driver)
    tmdb_page.open()

    tmdb_page.click_popular_button()

    tmdb_api = get_tmdb_api()
    movies_based_on_popularity_response = tmdb_api.get_movies_based_on_popularity(page=1)
    movies_based_on_popularity_response.assert_response_status_code(200)
    movies_based_on_popularity_response.assert_popularity_sorted_movie_names()

    # Verify whether the titles that shown in UI based on the API response
    movie_names = movies_based_on_popularity_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

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
    filtered_movies_response.assert_popularity_sorted_movie_names()

    # Verify whether the titles that shown in UI based on the API response
    movie_names = filtered_movies_response.get_movie_names()
    tmdb_page.verify_shown_titles(movie_names)

def test_sorted_movie_with_2_additional_genre_and_remove_1_genre(driver):
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
    filtered_movies_response.assert_popularity_sorted_movie_names()

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
    filtered_movies_response.assert_popularity_sorted_movie_names()

    # Verify whether the titles that shown in UI based on the API response
    movie_names = filtered_movies_response.get_movie_names()
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
    tv_show_based_on_popularity_response.assert_popularity_sorted_tv_show_names()

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = tv_show_based_on_popularity_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

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
    filtered_tv_show_response.assert_popularity_sorted_tv_show_names()

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = filtered_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)

def test_sorted_tv_show_with_2_additional_genre_and_remove_1_genre(driver):
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
    filtered_tv_show_response.assert_popularity_sorted_tv_show_names()

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
    filtered_tv_show_response.assert_popularity_sorted_tv_show_names()

    # Verify whether the titles that shown in UI based on the API response
    tv_show_names = filtered_tv_show_response.get_tv_show_names()
    tmdb_page.verify_shown_titles(tv_show_names)