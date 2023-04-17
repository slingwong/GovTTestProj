import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver: webdriver


class CSV:
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
            .until(ec.element_to_be_clickable((By.ID, 'dropdownMenuButton2')))

        driver.find_element(By.ID, 'dropdownMenuButton2').click()
        driver.find_element(By.LINK_TEXT, 'Upload a csv file').click()

    @staticmethod
    def create_csv_file():
        url = "http://localhost:9997"
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


class Search:
    @staticmethod
    def list_all():
        global driver
        url = "http://localhost:9997"
        driver = webdriver.Chrome()

        driver.get(url + "/login")
        driver.find_element(By.ID, 'username-in').send_keys('gov')
        driver.find_element(By.ID, 'password-in').send_keys('gov')
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    @staticmethod
    def list_all_button():
        list_all_btn = "//button[@value='List ALL']"
        WebDriverWait(driver, timeout=10) \
            .until(ec.element_to_be_clickable((By.XPATH, list_all_btn)))
        driver.find_element(By.XPATH, list_all_btn).click()

    @staticmethod
    def table_display():
        WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located((By.ID, 'search-all-table_filter')))
        assert driver.find_element(By.ID, 'search-all-table_filter').is_displayed()
        driver.implicitly_wait(30)
        print("Table display on page successfully")

    @staticmethod
    def table_row():
        num_rows = len(driver.find_elements(By.XPATH, '//*[@id="search-all-table"]/tbody/tr'))
        print("Rows in table are " + repr(num_rows))
        return num_rows

    @staticmethod
    def search_hero(hero):
        search_box = WebDriverWait(driver, timeout=10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="search-all-table_filter"]/label/input')))
        search_box.clear()
        search_box.send_keys(hero)
        WebDriverWait(driver, timeout=10).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="search-all-table_processing"]')))

    @staticmethod
    def result_display():
        WebDriverWait(driver, timeout=10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="search-all-table'
                                                                                          '"]/tbody/tr/td')))
        assert driver.find_element(By.XPATH, '//*[@id="search-all-table"]/tbody/tr/td').is_displayed()
        print("Result display on page successfully")

    @staticmethod
    def get_search_result():
        search_result = driver.find_element(By.XPATH, '//*[@id="search-all-table"]/tbody/tr/td').text
        return search_result

    @staticmethod
    def get_no_record():
        search_record = driver.find_element(By.XPATH,
                                            '//*[@id="search-all-table_info"]').text
        return search_record

    @staticmethod
    def get_search_name():
        search_result = driver.find_element(By.XPATH, '//*[@id="search-all-table"]/tbody/tr[1]/td[2]').text
        return search_result


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


class TaxRelief:
    @staticmethod
    def generate_tax():
        global driver
        url = "http://localhost:9997"
        driver = webdriver.Chrome()

        driver.get(url + "/login")
        driver.find_element(By.ID, 'username-in').send_keys('bk')
        driver.find_element(By.ID, 'password-in').send_keys('bk')
        driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    @staticmethod
    def tax_generate_button():
        driver.find_element(By.ID, 'tax_relief_btn').click()
