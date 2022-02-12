from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

from app.core.action import *
from app.core.main import *
from app.core.accounts import *

def _start():
    bot(accounts[0])
    # bot(accounts[1])

def bot(acc):
    core(acc)
    # _acc = core(acc)
    # _d = _acc.get_driver()
    # core.change_web("https://www.google.com/")
    # core.click("Google Login")
    core.change_web("https://myaccount.google.com/email")
    core.get_text("/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/article/div/div/div/div/ul/li/div[1]/div/div")
    # core._close()


#     login_success(driver, email)

# def login_success(driver, email):

#     change_web(driver, "https://wallet.wax.io/")
#     click(driver, "/html/body/div[1]/div/div/div/div[1]/div/div[3]/div[1]/div[2]/button/div/img")
#     target_name = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[2]").text
#     print(target_name)
    # if email == target_name:
        # print("Login Success")
    # else:
        # print("Login Fail")