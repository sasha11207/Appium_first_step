import pytest
import allure
from appium import webdriver

APP_PATH_V8 = ROOT_DIR + "/data/apk/v8a.apk"


@pytest.yield_fixture(scope='function', autouse=True)
def setup_suite(request):
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'Redmi'
    desired_caps['autoGrantPermissions'] = True
    desired_caps['app'] = APP_PATH_V8
    desired_caps['language'] = 'en'
    desired_caps['locale'] = 'US'
    desired_caps['uiautomator2ServerLaunchTimeout'] = 100000
    desired_caps['uiautomator2ServerInstallTimeout'] = 100000
    desired_caps['newCommandTimeout'] = 10000
    desired_caps['fullReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    driver.set_network_connection(6)
    yield driver
    today = datetime.datetime.today()
    filename = today.strftime("%Y-%m-%d-%H:%M")
    if request.session.testsfailed != failed_before:
        test_name = request.node.name + "-" + filename
        allure.attach(driver.save_screenshot(ROOT_DIR + "/allure/{}.png".
                                             format(test_name)))
    if driver:
        driver.quit()


class Helper:

    @staticmethod
    def get_driver():
        return driver
