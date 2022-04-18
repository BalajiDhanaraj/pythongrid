import pytest
from selenium import webdriver


"""  IN Terminal pytest (filename- like test_markers) -n(its define the no of parallel run we want"""
# driver = None
# @pytest.fixture(scope='module')
# def init_driver():
#     print("-------------------setup----------------------")
#     global driver
#     driver = webdriver.Chrome(
#         executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/grid/chromedriver")
#     driver.implicitly_wait(10)
#     driver.get("http://www.google.com")
#
#     yield
#     print("----------------------quit----------------------")
#     driver.quit()
#
# def test_google_title(init_driver):
#     assert driver.title == "Google"
#
#
# # def test_FB(init_driver):
# #     assert driver.title == "Facebook – log in or sign up"

#
# @pytest.fixture(params=['chrome'],scope='class')
# def init_driver(request):
#     print("-------------------setup----------------------")
#     driver = webdriver.Chrome(
#         executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/grid/chromedriver")
#     request.cls.driver = driver
#     yield
#     print("----------------------quit----------------------")
#     driver.quit()


@pytest.mark.usefixtures("init_driver")
class Base:
    pass

class Test_google(Base):

    def test_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"