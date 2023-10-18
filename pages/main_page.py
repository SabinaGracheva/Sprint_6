from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def click_accordion_button(self, locator_button):
        self.find_element(locator_button).click()

    def check_accordion_text(self, locator_text):
        accordion_text = self.find_element(locator_text).text
        return accordion_text

    def click_to_button_order(self, button_order):
        button = self.visibility_of_element_located(button_order)
        button.click()

    def click_on_logo_yandex(self):
        self.visibility_of_element_located(MainPageLocators.LOCATOR_LOGO_YANDEX).click()

    def check_to_yandex_page(self):

