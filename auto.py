from typing import ContextManager
from selenium import webdriver 
from selenium import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

mail ="< enter your mail>"
password = "< enter your password >"

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get('< enter your course link >')

wait = 10

driver.find_element_by_id("email").send_keys(mail)
driver.find_element_by_id("revealable-password").send_keys(password)

driver.implicitly_wait(30)
driver.find_element_by_css_selector(".vds-button--primary").click()

driver.implicitly_wait(30)
pop = driver.find_element_by_class_name("vds-modal__close-button").click()
# WebDriverWait(driver, wait).until(wait)
driver.implicitly_wait(30)


while True:
    try:
        next_btn = "._main--footer-container--3vC-_ .vds-button--secondary"
        # next_btn = "vds-button--secondary"_
        # WebDriverWait(driver, dellay).until(dellay)
        delay = driver.find_element_by_css_selector(next_btn).click()
        driver.implicitly_wait(30)
    except:
        next_btn = ".vds-button--primary"
        # next_btn = "vds-button--secondary"_
        # WebDriverWait(driver, dellay).until(dellay)
        delay = driver.find_element_by_css_selector(next_btn).click()
        driver.implicitly_wait(30)






#link = driver.find_element_by_class_name("vds-button vds-button--secondary")

#link.click()    