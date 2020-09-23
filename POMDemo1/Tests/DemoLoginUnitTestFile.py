from selenium import webdriver
import unittest
import time
from POMDemo1.Pages.LoginPage import LoginPage
from POMDemo1.Pages.HomePage import HomePage
import HtmlTestRunner
import os
import sys

sys.path.append(os.path.join(os.path.dirname("__find__"), "..", ".."))


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/cp/PycharmProjects/SeleniumPOM/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        Log = LoginPage(driver)
        Log.enter_username("Admin")
        # time.sleep(3)
        Log.enter_password("admin123")
        # time.sleep(3)
        Log.enter_login()

        Home = HomePage(driver)
        Home.ClickWelcome()
        Home.ClickLogout()

        # driver.find_element_by_id("txtUsername").clear()
        # time.sleep(3)
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").clear()
        # time.sleep(3)
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()
        # x = driver.title
        # assert x == 'OrangeHRM'
        # print(x)

    # def test_tearDown():
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Accomplished")

    # if "__name__" == "__main__":
    if __name__ == '__main__':
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/cp/PycharmProjects/SeleniumPOM/POMDemo1/Reports"))
