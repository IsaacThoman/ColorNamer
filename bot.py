from selenium import webdriver
import subprocess
import pynput
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
import time

x = 1
while True:
    driver = webdriver.Firefox()
    driver.get("https://colornames.org/random")
    elem = driver.find_element_by_name("proposedName")
    elem.clear()
    elem.send_keys("i don't like ryan")
    subprocess.Popen('powershell.exe .\enter.ps1')
    time.sleep(5)
    driver.close()
    time.sleep(1)








