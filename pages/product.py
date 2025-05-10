from selenium.webdriver.common.by import By

class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == title


    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//a[text() = "Samsung galaxy s6"]')
        galaxy_s6.click()