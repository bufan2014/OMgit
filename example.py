#encoding:utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("http://www.baidu.com")
time.sleep(0.2)
browser.find_element_by_id("kw1").send_keys("selenium")
time.sleep(0.2)
browser.find_element_by_id("su1").click()
print browser.title
browser.quit()