import logging, requests


class BaseApi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://api.themoviedb.org/3"
        self.api_key = "add494e96808c55b3ee7f940c9d5e5b6"

    def get_method(self, endpoint, **kwargs):
        url = self.base_url + endpoint + f"api_key={self.api_key}"

        self.logger.info("GET " + url)
        self.logger.info(f"REQUEST {kwargs}")

        return requests.get(url, **kwargs)


class BaseResponse:
    def __init__(self, response):
        self.logger = logging.getLogger(__name__)
        self.response = response
        self.response_data = self.response.json()