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
driver.get("https://www.emag.ro/cart/products?ref=cart")
test = driver.find_element_by_xpath("//*[@id=\"cartProductsPage\"]/div[3]/div/div/div[3]/a")
ActionChains(driver).move_to_element(test).click().perform()

# Fill in all delivery/personal data info fields

test = driver.find_element_by_xpath("//button[@type='submit']")
ActionChains(driver).move_to_element(test).click().perform()

# Verify the delivery data info

test = driver.find_element_by_xpath("//button[@type='submit']")
ActionChains(driver).move_to_element(test).click().perform()

