#-*- coding: UTF-8 -*- 
'''作用--从商品详情页加购物车并查看购物车
   状态--done'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Jiagouwu01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "http://www.tsdian.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_jiagouwu01(self):
        driver = self.driver
        driver.get(self.base_url + "product-10375.html")
        driver.find_element_by_xpath("//label[@class='item-size']").click()
        time.sleep(1)
        #driver.find_element_by_css_selector("label.item-size > span").click()
        
        driver.find_element_by_id("det_img_variant_image_10375_329_601").click()
        time.sleep(1)
        driver.find_element_by_id("button_cart_10375").click()
        
        driver.find_element_by_link_text("查看购物车").click()
        time.sleep(3)

        driver.find_element_by_link_text("去结算").click()
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