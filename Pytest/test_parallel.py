import pytest
from selenium import webdriver


def test_google():
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/grid/chromedriver")
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_FB():
    driver = webdriver.Chrome(
        executable_path="/Volumes/Macintosh HD/For Mac/python project/pythongrid/grid/chromedriver")
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()











