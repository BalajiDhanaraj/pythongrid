from configparser import ConfigParser

## reading the config file

# config = ConfigParser()
# config.read("config.ini")
#
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))



def readConfig(section,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section,key)


print(readConfig("locator","username"))