from src.api.base import BaseApi, BaseResponse
import random


class TmdbApi(BaseApi):
    def get_movie_genre_list(self):
        endpoint = "/genre/movie/list?"

        response = self.get_method(endpoint)

        return GetMovieGenreListResponse(response)

    def get_tv_show_genre_list(self):
        endpoint = "/genre/tv/list?"

        response = self.get_method(endpoint)

        return GetTvShowGenreListResponse(response)

    def get_movies_based_on_popularity(self, page):
        endpoint = f"/movie/popular?page={page}&"

        response = self.get_method(endpoint)

        return GetMoviesResponse(response)

    def get_tv_show_based_on_popularity(self, page):
        endpoint = f"/tv/popular?page={page}&"

        response = self.get_method(endpoint)

        return GetTvShowResponse(response)

    def get_filtered_movies(self, sort_by, genres, start_date="1900-01-01", end_date="2025-12-31", rating=0, page=1):
        endpoint = (
            f"/discover/movie?sort_by={sort_by}.desc&"
            f"release_date.gte={start_date}&release_date.lte={end_date}&"
            f"vote_average.gte={rating}&vote_average.lte=5&"
            f"page={1}&"
        )

        genre_ids = ""
        for genre in genres:
            genre_ids += f"{genre['id']},"

        endpoint += f"with_genres={genre_ids[:-1]}&"


        response = self.get_method(endpoint)

        return GetMoviesResponse(response)

    def get_filtered_tv_show(self, sort_by, genres, start_date="1900-01-01", end_date="2025-12-31", rating=0, page=1):
        endpoint = (
            f"/discover/tv?sort_by={sort_by}.desc&"
            f"release_date.gte={start_date}&release_date.lte={end_date}&"
            f"vote_average.gte={rating}&vote_average.lte=5&"
            f"page={1}&"
        )

        genre_ids = ""
        for genre in genres:
            genre_ids += f"{genre['id']},"

        endpoint += f"with_genres={genre_ids[:-1]}&"


        response = self.get_method(endpoint)

        return GetTvShowResponse(response)

    def get_movies_based_on_trend(self, page=1):
        endpoint = f"/trending/movie/week?page={page}&"

        response = self.get_method(endpoint)

        return GetMoviesResponse(response)

    def get_tv_show_based_on_trend(self, page=1):
        endpoint = f"/trending/tv/week?page={page}&"

        response = self.get_method(endpoint)

        return GetTvShowResponse(response)

    def get_newest_movie(self, page=1):
        endpoint = f"/movie/now_playing?page={page}&"

        response = self.get_method(endpoint)

        return GetMoviesResponse(response)

    def get_newest_tv_show(self, page=1):
        endpoint = f"/tv/on_the_air?page={page}&"

        response = self.get_method(endpoint)

        return GetTvShowResponse(response)
    
    def get_top_rated_movie(self, page=1):
        endpoint = f"/movie/top_rated?page={page}&"

        response = self.get_method(endpoint)

        return GetMoviesResponse(response)
    
    def get_top_rated_tv_show(self, page=1):
        endpoint = f"/tv/top_rated?page={page}&"

        response = self.get_method(endpoint)

        return GetTvShowResponse(response)


class GetMovieGenreListResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"Response status code : {self.response.status_code}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )

    def get_random_genres(self, count):
        random_genres = random.sample(self.response_data['genres'], count)

        self.logger.info(f"Random genres : {random_genres}")

        return random_genres


class GetTvShowGenreListResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"Response status_code : {self.response.status_code}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )

    def get_random_genres(self, count):
        random_genres = random.sample(self.response_data['genres'], count)

        self.logger.info(f"Random genres : {random_genres}")
        
        return random_genres


class GetMoviesResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"Response status_code : {self.response.status_code}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )

    def get_movie_names(self):
        movie_names = []

        for result in self.response_data["results"]:
            movie_names.append(result["title"])

        self.logger.info(f"Movie names : {movie_names}")

        return movie_names

    def assert_genres_in_response(self, genres):
        self.logger.info(f"Genre to compare {genres}")

        for genre in genres:
            for result in self.response_data["results"]:
                self.logger.info(f"Assert genre : {result['title']} with {result['genre_ids']} has Genre : {genre['id']}")

                assert genre["id"] in result["genre_ids"], (
                    f"{genre['id']} is not in expected result: {result['genre_ids']}"
                )


class GetTvShowResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"Response status_code : {self.response.status_code}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )

    def get_tv_show_names(self):
        tv_show_names = []

        for result in self.response_data["results"]:
            tv_show_names.append(result["name"])

        self.logger.info(f"Tv show names : {tv_show_names}")

        return tv_show_names

    def assert_genres_in_response(self, genres):
        self.logger.info(f"Genre to compare {genres}")

        for genre in genres:
            for result in self.response_data["results"]:
                self.logger.info(f"Assert genre : {result['name']} with {result['genre_ids']} has Genre : {genre['id']}")

                assert genre["id"] in result["genre_ids"], (
                    f"{genre['id']} is not in expected result: {result['genre_ids']}"
                )
