import uuid
from typing import Optional, Literal

from config.env import Env
from support.http.client import Request


class AppAutomateApi:
    def __init__(self):
        """Create a new instance of the AppAutomateApi class."""
        self.__request = Request(Env.API_BROWSERSTACK)
        self.__credentials = (
            Env.BROWSERSTACK_USERNAME,
            Env.BROWSERSTACK_ACCESS_KEY,
        )

    def upload_app(
        self,
        file_name: str,
        file_path: str,
        custom_id: Optional[str] = None
    ) -> str:
        """Upload the app to BrowserStack and get the app_url.

        :param file_name: (str) The name of the app.
        :param file_path: (str) The path to the app.
        :param custom_id: (str) The custom_id to identify the app.
        :return: (str) The app_url.
        """
        custom_id = custom_id or uuid.uuid4()
        files = {
            "file": (file_name, open(file_path, "rb")),
            "custom_id": (None, custom_id),
        }
        response = self.__request.post(
            endpoint="/upload",
            files=files,
            auth=self.__credentials,
        )
        response.raise_for_status()

        return response.json()["app_url"]


    def recent_apps_from_storage(
        self, custom_id: Optional[str] = None, limit: int = 10
    ) -> list:
        """Get the recent apps.

        :param custom_id: (str) The custom_id to identify the app.
        :param limit: (int) The number of apps to be returned.
        :return: (dict) The recent apps.
        """
        params = {"limit": limit}
        if custom_id:
            params["custom_id"] = custom_id
        response = self.__request.get(
            endpoint="/recent_apps",
            params=params,
            auth=self.__credentials,
        )
        response.raise_for_status()
        return response.json()

    def get_last_app_url_by_platform_from_storage(
        self, platform: Literal["ios", "android"]
    ) -> str:
        """Get the last app url by platform.

        :param platform: (str) The platform of the app.
        :return: (str) The last app url.
        """
        apps_from_storage = self.recent_apps_from_storage()
        android_or_ios = ".apk" if platform == "android" else ".ipa"
        if apps_from_storage:
            for app in apps_from_storage:
                app_name: str = app["app_name"]
                if app_name.endswith(android_or_ios):
                    return app["app_url"]
        else:
            raise Exception("No application found in the storage")
