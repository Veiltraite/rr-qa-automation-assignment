from src.api import get_tmdb_api


def test_get_movie_genre_list():
    tmdb_api = get_tmdb_api()
    movie_genre_list_response = tmdb_api.get_movie_genre_list()

    movie_genre_list_response.assert_response_status_code(200)

def test_get_tv_show_genre_list():
    tmdb_api = get_tmdb_api()
    tv_show_genre_list_response = tmdb_api.get_tv_show_genre_list()

    tv_show_genre_list_response.assert_response_status_code(200)