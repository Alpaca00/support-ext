import warnings

import requests
from requests import Session


class Request:
    def __init__(self, url: str):
        """Create a new instance of the Request class.

        :param url: (str) The URL to be requested.
        """
        self.url = url
        self.request = requests

    @property
    def session(self) -> Session:
        """Returns a session attribute of the 'requests' module with a proxy if proxy is True."""
        with self.request.Session() as session:
            with warnings.catch_warnings():
                warnings.simplefilter(action="ignore", category=ResourceWarning)
                return session

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Sends a GET request.

        :param endpoint: (str) The endpoint to be requested.
        :param kwargs: (dict) Optional arguments that request takes.
        :return: (Response) The response of the request.
        """
        return self.session.get(url=f"{self.url}{endpoint}", **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """Sends a POST request.

        :param endpoint: (str) The endpoint to be requested.
        :param kwargs: (dict) Optional arguments that request takes.
        :return: (Response) The response of the request.
        """
        return self.session.post(url=f"{self.url}{endpoint}", **kwargs)
