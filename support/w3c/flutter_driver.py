from typing import Callable

from appium_flutter_finder import FlutterFinder, FlutterElement


class BaseFlutterDriver:
    """Flutter driver finder base class."""

    __slots__ = ["driver", "_finder", "_element"]

    def __init__(self, driver: any):
        self.driver = driver
        self._finder = FlutterFinder()
        self._element = lambda element: FlutterElement(self.driver, element)

    @property
    def finder(self) -> FlutterFinder:
        """Return finder instance attribute."""
        return self._finder

    @property
    def element(self) -> Callable:
        """Return element instance attribute."""
        return self._element
