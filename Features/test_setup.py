import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver


class SessionID:
    @staticmethod
    def get_j_session_id(username, password):
        global driver
        url = "http://localhost:9997"

        driver = webdriver.Chrome()

        driver.get(url + "/login")
        driver.find_element(By.ID, 'username-in').send_keys(username)
        driver.find_element(By.ID, 'password-in').send_keys(password)
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()

        cookies = driver.get_cookie("JSESSIONID")

        driver.quit()

        return cookies["value"]


class UploadFile:
    @staticmethod
    def upload_csv_file():
        global driver
        url = "http://localhost:9997"

        driver = webdriver.Chrome()
        driver.get(url + "/login")
        driver.find_element(By.ID, 'username-in').send_keys('clerk')
        driver.find_element(By.ID, 'password-in').send_keys('clerk')
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()

        WebDriverWait(driver, timeout=10) \
            .until(expected_conditions.element_to_be_clickable((By.ID, 'dropdownMenuButton2')))

        driver.find_element(By.ID, 'dropdownMenuButton2').click()
        driver.find_element(By.LINK_TEXT, 'Upload a csv file').click()

        WebDriverWait(driver, timeout=10) \
            .until(expected_conditions.element_to_be_clickable((By.ID, 'upload-csv-file')))
        driver.quit()