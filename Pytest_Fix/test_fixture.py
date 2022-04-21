
import pytest
from selenium import webdriver





@pytest.mark.usefixtures("init_driver")
class Base:
    pass

class Test_google(Base):

    def test_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
