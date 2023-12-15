from support.browserstack_cloud.app_automate import AppAutomateApi


class CloudsMixin:
    """Mixin class for clouds."""

    def __init__(self):
        self.browserstack_app_automate = AppAutomateApi()
