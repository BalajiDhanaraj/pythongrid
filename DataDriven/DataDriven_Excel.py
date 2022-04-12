import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver as driver
import pytest

# parallel test

@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


def get_data():
    return [

        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf"),
        ("info@way2automation.com", "sdfsdf")

    ]

def setup_function():
    global driver
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")
    driver.get("http://facebook.com")


def teardown_function():
    driver.quit()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username, password, get_browser):
    driver = get_browser
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    allure.attach(driver.get_screenshot_as_png(),name="dologin",attachment_type=AttachmentType.png)
