import pytest
from driver_factory import DriverFactory

@pytest.fixture(scope='class')
def init_driver(request, appium_env, platform, app):
    try:
        request.cls.appium_env = appium_env
        request.cls.platform = platform
        request.cls.app = app
        start_app_with_driver_init(request)
        yield
        # quit appium driver
        print("driver quit")
        request.cls.driver.quit()
    finally:
        pass

def start_app_with_driver_init(request):
    print("driver init")
    df = DriverFactory()
    appium_driver = df.create_driver(request.cls.appium_env, request.cls.platform, request.cls.app)
    if appium_driver is None:
        pytest.fail('appium Driver is None!')
    request.cls.driver = appium_driver

@pytest.fixture(scope='function', autouse=True)
def get_current_test_name(request):
    return str(request.node.name)
    
@pytest.fixture(scope='session')
def appium_env(request):
    """
    Use the command line argument as a fixture function
    :param request:
    :return: --appium_env (command line option)
    """
    return request.config.getoption("--appium_env")


@pytest.fixture(scope='session')
def platform(request):
    """
    Use the command line argument as a fixture function
    :param request:
    :return: --platform (command line option)
    """
    return request.config.getoption("--platform")


@pytest.fixture(scope='session')
def app(request):
    return request.config.getoption("--app")

def pytest_addoption(parser):
    parser.addoption("--appium_env", action="store", help="--appium_env: LOCAL, BROWSERSTACK, etc")
    parser.addoption("--platform", action="store", help="--platform: ios or android")
    parser.addoption("--app", action="store",
                     help="--app: Path to the test app. Takes app from the apps folder if not specified")
    
