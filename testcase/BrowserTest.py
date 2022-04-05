from selenium import webdriver

# driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")
from selenium.webdriver import DesiredCapabilities

remote_url = "http://localhost:6666/wd/hub"

driver = webdriver.Remote(command_executor=remote_url,desired_capabilities={"browserName":"chrome"})

driver.get("http://way2automation.com")


title = driver.title

print(title)

assert "Selenium" in title

driver.close()

driver.quit()