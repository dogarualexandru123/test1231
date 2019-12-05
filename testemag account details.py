import sys
import re
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from airtest_selenium.proxy import WebChrome
from pynput.keyboard import Key, Controller
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains



def click_element(drv, elm):
    ActionChains(drv).move_to_element(elm).click().perform()


options = Options()
#options.add_argument("--headless")
options.add_argument("window-size=1366x768")
driver = WebChrome(options=options)
driver.implicitly_wait(5)
driver.delete_all_cookies()

driver.get("chrome-search://local-ntp/local-ntp.html")
driver.get("https://www.emag.ro/user/account")

driver.find_element_by_id("email").send_keys("kipesoc676@newmail.top")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()


driver.find_element_by_xpath("//input[@type='password']").send_keys("Test123@")
driver.find_element_by_xpath("/html/body/form/div[4]/div/button").click()


test = driver.find_element_by_xpath("//button[@type='button']")
ActionChains(driver).move_to_element(test).click().perform()

driver.find_element_by_xpath("//input[@placeholder='ex: popalex3']").click()
driver.find_element_by_xpath("//input[@placeholder='ex: popalex3']").click()



driver.find_element_by_xpath("//input[@placeholder='ex: popalex3']").send_keys("alex")
driver.find_element_by_name("telephone1").send_keys("0771496456")

driver.find_element_by_name("telephone1").send_keys(u'\ue007')


driver.find_element_by_xpath("//button[@type='button']").click()


