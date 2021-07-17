from selenium import webdriver
import time
import unittest

class TestWebDriver(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path='D:\Python Projects\drivers\geckodriver.exe')
        driver.get("https://www.google.com/")
    
    def test1(self):
        driver.find_element_by_name("q").send_keys("Mahesh Babu")
        time.sleep(5)
        driver.find_element_by_name("btnK").click()
        time.sleep(5)
        driver.find_element_by_class_name("LC20lb").click()
        time.sleep(5)
    
    def tearDown(self):
        driver.close()
        

unittest.main()

 

