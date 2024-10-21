import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from pyunitreport import HTMLTestRunner
import time
from selenium.webdriver.common.by import By

class FirstTest(unittest.TestCase):
    driver = None
    __id_button_login = "login-button"
    __xpath_input_user = '//*[@id="user-name"]'
    __id_input_password = "password"
    __xpath_error_message = '//*[@data-test="error"]'
    __xpath_product_page_title = '//*[@class="title"]'

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test1_open_browser(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        element = driver.find_element(By.ID, self.__id_button_login).is_displayed()
        self.assertTrue(element)
        time.sleep(30)

    def test2_login_failed(self):
        driver = self.driver
        user = "standard_user"
        password = "secret_sayyuce"  # contrasena incorrecta
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, self.__xpath_input_user).send_keys(user)
        driver.find_element(By.ID, self.__id_input_password).send_keys(password)
        driver.find_element(By.ID, self.__id_button_login).click()
        error_message = driver.find_element(By.XPATH, self.__xpath_error_message).is_displayed()
        self.assertTrue(error_message, "No se mostró el mensaje de error")
        time.sleep(10)

    def test3_login_success(self):
        driver = self.driver
        user = "standard_user"
        password = "secret_sauce"  # contrasena correcta
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, self.__xpath_input_user).send_keys(user)
        driver.find_element(By.ID, self.__id_input_password).send_keys(password)
        driver.find_element(By.ID, self.__id_button_login).click()
        product_title = driver.find_element(By.XPATH, self.__xpath_product_page_title).is_displayed()
        self.assertTrue(product_title, "No se redirigió a la página de productos")
        time.sleep(10)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Prueba'))
