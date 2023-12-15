from typing import Literal

from appium import webdriver as appium_webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions



class WebDriver:
    """Class to create a new WebDriver instance."""

    @staticmethod
    def connection(
        command_executor: str,
        options: AppiumOptions,
        **kwargs
    ) -> appium_webdriver.Remote:
        """Create a new WebDriver instance.

        :param command_executor: str, url to connect to appium server.
        :param options: AppiumOptions, options to create the driver.
        :kwargs: Optional[Dict] = None
        :return: Appium Webdriver.
        """
        return appium_webdriver.Remote(
            command_executor=command_executor, options=options, **kwargs
        )


def webdriver_instance(
    capabilities: dict,
    command_executor: str,
    platform: Literal["android", "ios"],
    automation_name: str = "Flutter",
    **kwargs
) -> appium_webdriver.Remote:
    """Method to create a new WebDriver instance.

    :param capabilities: dict, capabilities to create the driver.
    :param command_executor: str, url to connect to appium server.
    :param platform: Literal["android", "ios"], platform to create the driver.
    :param automation_name: str, automation name to create the driver.
    :kwargs: Optional[Dict] = None
    :return: Appium Webdriver.
    """
    if platform == "android":
        options = UiAutomator2Options()
        options = options.load_capabilities(capabilities)
        options = options.set_capability("automationName", automation_name)
        return WebDriver.connection(
            command_executor=command_executor,
            options=options,
            **kwargs
        )
    elif platform == "ios":
        options = XCUITestOptions()
        options = options.load_capabilities(capabilities)
        options = options.set_capability("automationName", automation_name)
        return WebDriver.connection(
            command_executor=command_executor,
            options=options,
            **kwargs
        )
    else:
        raise ValueError("Platform not supported or not found.")
