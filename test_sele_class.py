from selenium import webdriver
import time
import unittest

class HMSLoginLogoutDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Firefox(executable_path='D:\Python Projects\drivers\geckodriver.exe')
        driver.get("http://www.seleniumbymahesh.com/")
        time.sleep(5)
    
    def test_login(self):
        driver.find_element_by_link_text("HMS").click()
        time.sleep(5)
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        time.sleep(10)
    
    def test_logout(self):
        driver.find_element_by_link_text("Logout").click()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        driver.close()

unittest.main()

 

