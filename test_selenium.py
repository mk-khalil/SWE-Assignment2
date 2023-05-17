import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://127.0.0.1:5000/'

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        driver = self.driver
        driver.get(self.base_url)

        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        username.send_keys('test')
        password.send_keys('test')
        submit_button.click()

        time.sleep(1)

        welcome_message = driver.find_element(By.TAG_NAME, 'p')
        self.assertEqual(welcome_message.text, 'Welcome, test!')

    def test_unsuccessful_login(self):
        driver = self.driver
        driver.get(self.base_url)

        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        username.send_keys('wrong')
        password.send_keys('wrong')
        submit_button.click()

        time.sleep(1)

        alert = driver.find_element(By.TAG_NAME, 'p')
        self.assertEqual(alert.text, 'Invalid credentials. Please try again.')

    def test_logout(self):
        driver = self.driver
        driver.get(self.base_url)

        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        submit_button = driver.find_element(By.TAG_NAME, 'button')

        username.send_keys('test')
        password.send_keys('test')
        submit_button.click()

        time.sleep(1)

        logout_button = driver.find_element(By.TAG_NAME, 'button')
        logout_button.click()

        time.sleep(1)

        self.assertEqual(driver.current_url, self.base_url)

if __name__ == '__main__':
    unittest.main()