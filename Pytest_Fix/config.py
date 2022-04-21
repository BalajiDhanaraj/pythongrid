import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def init_driver(request):
    print("-------------------setup----------------------")
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/Pytest/chromedriver")
    request.cls.driver = driver
    yield
    print("----------------------quit----------------------")
    driver.close()