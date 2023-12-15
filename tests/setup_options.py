import json
import uuid
from typing import Literal

from config.env import Env
from support.w3c.webdriver_instance import webdriver_instance
from tests.clouds_mixin import CloudsMixin


class CloudConfig:
    """Class to set up the remote connection."""
    CAPABILITIES = {
        "platformName": Env.PLATFORM_NAME,
        "os_version": Env.OS_VERSION,
        "deviceName": Env.DEVICE_NAME,
        "maxInstances": 1,
        "project": "Foodtech",
        "build": str(uuid.uuid4()),
        "name": "Test to reproduce the bug",
        "real_mobile": True,
        "appiumVersion": "2.0.1",
        "browserstack.local": "false",
        "automationName": "Flutter",
        "autoGrantPermissions": True,
        "autoAcceptAlerts": True,
        "appWaitForLaunch": True,
        "noReset": False,
        "browserstack.idleTimeout": 300,
        "browserstack.debug": True,
        "browserstack.networkLogs": True,
        "retryBackoffTime": 3000,
        "appWaitDuration": 30000,
    }


class WebdriverOptions:
    """Class to set up the webdriver options."""

    def __init__(
        self,
        platform: Literal["android", "ios"],
        cloud_options: Literal["browserstack", "saucelabs", "aws"] = "browserstack",
    ):
        """Constructor method."""
        self._platform = platform
        self.__clouds_mixin = CloudsMixin()
        if cloud_options == "browserstack":
            self._recent_app = self.__clouds_mixin.browserstack_app_automate.get_last_app_url_by_platform_from_storage(self._platform)  # noqa

    def get_appium_driver(self) -> webdriver_instance:
        """Set up the options."""
        capabilities = CloudConfig.CAPABILITIES
        capabilities.update({"app": self._recent_app})
        print(json.dumps(capabilities, indent=2))
        return webdriver_instance(
            capabilities=capabilities,
            command_executor=Env.APPIUM_BROWSERSTACK,
            platform=self._platform,
        )
