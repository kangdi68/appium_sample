from appium import webdriver
from appium.webdriver.appium_connection import AppiumConnection
from requests.adapters import Retry
from selenium.common.exceptions import WebDriverException

android_common_desired_capabilities = {
    "platformName": "Android",
    "appium:automationName": "uiautomator2",
    "appium:optionalIntentArguments": "--ez automation true",
    "appium:noReset": "false",
    "autoGrantPermissions": "true",
    "newCommandTimeout": 300
}

ios_common_desired_capabilities = {
    "platformName": "iOS",
    "appium:xcodeOrgId": "something",
    "appium:xcodeSigningId": "iPhone Developer",
    "appium:automationName": "XCUITest",
    "appium:noReset": "false",
    "startIWDP": "true",
    "newCommandTimeout": 300
}

class DriverFactory:

    def create_driver(self, appium_env, platform, app):
        """
        :param app: path to the test app (default is apps folder)
        :param appium_env: local or sauce or something else
        :param platform: iOS or Android
        :return: appium driver object
        """
        appium_host = 'http://localhost:4723/wd/hub'
        dc = dict()
        preset_device = {
                "appium:platformVersion": "os version",
                "appium:udid": "udid",
                "appium:deviceName": "model name"
            }
        dc = self.set_desired_capabilities(appium_env, platform, preset_device, app)
        retry_config = Retry(total=3,
                             backoff_factor=1,
                             status_forcelist=[500, 502, 503, 504])
        appium_executor = AppiumConnection(remote_server_addr=appium_host,
                                           init_args_for_pool_manager={
                                               "retries": retry_config
                                           })
        try:
            return webdriver.Remote(appium_executor, dc)
        except WebDriverException as error:
            print("WebDriverException=", error)

    def set_desired_capabilities(self, appium_env, platform, preset_device, app=None):
        _desired_caps = dict()
        if platform.lower() == constants.PLATFORM_IOS:
            _desired_caps.update(ios_common_desired_capabilities)
        else:
            _desired_caps.update(android_common_desired_capabilities)
        _desired_caps.update({
              'appium:app': app,
                    "fullReset": True
                })
        return _desired_caps
