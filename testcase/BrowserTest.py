from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Volumes/Macintosh HD/For Mac/python project/Browserdrivers/chromedriver")

# remote_url = "http://localhost:4444/wd/hub"

# driver = webdriver.Remote(command_executor=remote_url,desired_capabilities={"browserName":"firefox"})



driver.get("http://way2automation.com")


title = driver.title

print(title)

assert "Selenium" in title

driver.close()

driver.quit()