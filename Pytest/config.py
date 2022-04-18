import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    print("-------------------setup----------------------")
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/grid/chromedriver")
    request.cls.driver = driver
    yield
    print("----------------------quit----------------------")
    driver.quit()