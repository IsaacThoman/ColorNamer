from selenium import webdriver
import subprocess
import pynput
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://colornames.org/random")
elem = driver.find_element_by_name("proposedName")
elem.clear()
elem.send_keys("i don't like ryan")
time.sleep(3)


x = 1
while True:
    driver.close()
    driver = webdriver.Firefox()
    driver.get("https://colornames.org/random")
    elem = driver.find_element_by_name("proposedName")
    elem.clear()
    elem.send_keys("i don't like ryan")
    time.sleep(6)










