import unittest
import HtmlTestRunner
import time
from selenium import webdriver
import sys
sys.path.append("C:/Users/inasahu/PycharmProjects/POM_Python_Selenium")
from pageObjects.LoginPage import LoginPageClass


class LoginTest(unittest.TestCase):

    baseUrl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(
        executable_path="C:/Users/inasahu/PycharmProjects/POM_Python_Selenium/drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        loginPage = LoginPageClass(self.driver)
        loginPage.setUserName(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./reports"))

