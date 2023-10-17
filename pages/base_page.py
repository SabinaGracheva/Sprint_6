from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def presence_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator))

    def visibility_of_element_located(self, locator, time=10):
        self.scroll_to_element(self.presence_of_element_located(locator))
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):  #получить корректный урл
        return self.driver.current_url

    def switch_to_window(self, index_page):
        self.driver.switch_to.window(self.driver.window_handles[index_page])
