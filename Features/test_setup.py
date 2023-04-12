import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver


def upload_csv_file():
    global driver
    url = "http://localhost:9997"

    driver = webdriver.Chrome()

    driver.get(url + "/login")
    driver.find_element(By.ID, 'username-in').send_keys('clerk')
    driver.find_element(By.ID, 'password-in').send_keys('clerk')
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    WebDriverWait(driver, timeout=10) \
        .until(ec.element_to_be_clickable((By.ID, 'dropdownMenuButton2')))

    driver.find_element(By.ID, 'dropdownMenuButton2').click()
    driver.find_element(By.LINK_TEXT, 'Upload a csv file').click()


def create_csv_file():
    script_path = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(os.path.sep, script_path, "upload.csv")
    WebDriverWait(driver, timeout=10) \
        .until(ec.element_to_be_clickable((By.ID, 'upload-csv-file')))
    driver.find_element(By.ID, 'upload-csv-file').send_keys(csv_file)
    driver.find_element(By.XPATH, '//button[normalize-space()="Create"]').click()

    WebDriverWait(driver, timeout=10) \
        .until(ec.visibility_of_element_located(
        (By.XPATH, "//*[@id='notification-block']/descendant::h3")))

    result = driver.find_element(By.XPATH, "//*[@id='notification-block']/descendant::h3").text

    return result


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
