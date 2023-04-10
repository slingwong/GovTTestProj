from selenium import webdriver
from selenium.webdriver.common.by import By


class SessionID:
    @staticmethod
    def get_j_session_id(username, password):
        url = "http://localhost:9997"

        driver = webdriver.Chrome()

        driver.get(url + "/login")
        driver.find_element(By.ID, 'username-in').send_keys(username)
        driver.find_element(By.ID, 'password-in').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()

        cookies = driver.get_cookie("JSESSIONID")

        driver.quit()

        return cookies["value"]

"""
    @staticmethod
    def system_logout():
        driver = webdriver.Chrome()
        driver.find_element(By.CLASS_NAME, 'btn-small').click()
"""