import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

import pytest



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    remote_url = "http://192.168.1.6:4444"
    if request.param == "chrome":
       # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
       driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "chrome"})

    # if request.param == "firefox":
    #    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #    driver = webdriver.Remote(command_executor=remote_url, desired_capabilities={"browserName": "firefox"})

    driver.get("http://facebook.com")

    yield driver
    driver.quit()