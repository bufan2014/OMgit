#-*- coding:utf-8 -*_
'''作用--正向登录
   状态--done'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "http://www.tsdian.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(1)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("bufan001@test.com")
        driver.find_element_by_id("J_checkpsw").clear()
        driver.find_element_by_id("J_checkpsw").send_keys("bufan001")
        time.sleep(1)
        driver.find_element_by_name("dispatch[auth.login]").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(1)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("bufan001@test.com")
        driver.find_element_by_id("J_checkpsw").clear()
        driver.find_element_by_id("J_checkpsw").send_keys("bufan001")
        driver.find_element_by_id("rember").click()
        time.sleep(1)
        driver.find_element_by_name("dispatch[auth.login]").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(3)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
