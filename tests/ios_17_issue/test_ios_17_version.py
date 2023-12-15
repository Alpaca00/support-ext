import unittest

from config.env import Env
from support.w3c.flutter_driver import BaseFlutterDriver
from tests.setup_options import WebdriverOptions



class FlutterIOS17(unittest.TestCase):
    def setUp(self):
        """Setup for the test."""
        self.__driver = WebdriverOptions(
            platform=Env.PLATFORM_NAME
        ).get_appium_driver()
        self.flutter = BaseFlutterDriver(self.__driver)

    def tearDown(self):
        """Tear down the test."""
        self.flutter.driver.quit()

    def test_launch_on_ios_17_version(self):
        """Test to reproduce the bug #1047607 on iOS 17 version."""
        expected_text = "0"
        label = self.flutter.finder.by_value_key("counter--text-label")
        actual_text = self.flutter.element(label).text
        self.assertEqual(actual_text, expected_text)



if __name__ == '__main__':
    unittest.main()
