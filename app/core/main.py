from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


class core(object):
  def __init__(self, data):
    global _driver
    global _name
    _name = data["name"]
    self.email = data["email"]

    profile = webdriver.FirefoxProfile(f"C:\\Users\\prapa\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\{_name}")
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference("useAutomationExtension", False)
    profile.update_preferences()
    desired = DesiredCapabilities.FIREFOX
    _driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)
    print(f"USE {_name}")

  def get_driver():
    return _driver

  def get_name():
    return _name

  def click(_action):
    xpath = None
    if _action == "Google Login":
      xpath = "/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/a/img"
    _driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    print(_action)

  def change_web(href):
    _driver.get(href)
    time.sleep(3)

  def _close():
    _driver.close()
    print(f"BYE~ {_name}")

  def get_text(xpath):
    print(_driver.find_element_by_xpath(xpath))

    

