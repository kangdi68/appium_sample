import pytest
from driver_factory import DriverFactory

@pytest.fixture(scope='class')
def init_driver(request, appium_env, platform, app, app_id_cloud, desired_os_version):
    try:
        request.cls.appium_env = appium_env
        request.cls.platform = platform
        request.cls.app = app
        request.cls.app_id_cloud = app_id_cloud
        request.cls.desired_os_version = desired_os_version
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
    appium_driver = df.create_driver(request.cls.appium_env, request.cls.platform, request.cls.app,
                                     request.cls.app_id_cloud, request.cls.__name__, request.cls.desired_os_version)
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


@pytest.fixture(scope='session')
def app_id_cloud(request):
    return request.config.getoption("--app_id_cloud")


@pytest.fixture(scope='session')
def desired_os_version(request):
    return request.config.getoption("--desired_os_version")

def pytest_addoption(parser):
    parser.addoption("--appium_env", action="store", help="--appium_env: LOCAL, BROWSERSTACK, etc")
    parser.addoption("--platform", action="store", help="--platform: ios or android")
    parser.addoption("--app", action="store",
                     help="--app: Path to the test app. Takes app from the apps folder if not specified")
    parser.addoption("--app_id_cloud", action="store",
                     help="--app_id_cloud: automatically set after uploading app to device cloud")
    parser.addoption("--desired_os_version", action="store",
                     help="--desired_os_version: random or latest or specific version number")
