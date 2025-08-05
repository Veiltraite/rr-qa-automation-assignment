from src.api.base import BaseApi, BaseResponse


class TmdbApi(BaseApi):
    def get_movie_genre_list(self):
        endpoint = "/genre/movie/list?"

        response = self.get_method(endpoint)

        return GetMovieGenreListResponse(response)

    def get_tv_show_genre_list(self):
        endpoint = "/genre/tv/list?"

        response = self.get_method(endpoint)

        return GetTvShowGenreListResponse(response)


class GetMovieGenreListResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"response data : {self.response_data}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )


class GetTvShowGenreListResponse(BaseResponse):
    def assert_response_status_code(self, status_code):
        self.logger.info(f"response data : {self.response_data}")

        assert self.response.status_code == status_code, (
            f"Actual result: {self.response.status_code}, "
            f"is not equal to expected result: {status_code}"
        )
