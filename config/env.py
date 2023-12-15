import os

from dotenv import load_dotenv

load_dotenv()


class Env:
    """Class to set up the environment variables."""

    # ENVIRONMENT VARIABLES
    PLATFORM_NAME = os.environ.get("BROWSERSTACK_PLATFORM_NAME")
    DEVICE_NAME = os.environ.get("BROWSERSTACK_DEVICE_NAME")
    OS_VERSION = os.environ.get("BROWSERSTACK_OS_VERSION")
    BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME_REP")
    BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY_REP")

    # CONSTANTS
    APPIUM_BROWSERSTACK = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"  # noqa
    API_BROWSERSTACK = "https://api-cloud.browserstack.com/app-automate"
