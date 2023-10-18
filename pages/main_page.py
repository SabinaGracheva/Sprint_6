import allure

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Нажать на дроп-даун')
    def click_accordion_button(self, locator_button):
        self.find_element(locator_button).click()

    @allure.step('Проверить текст дроп-дауна')
    def check_accordion_text(self, locator_text):
        accordion_text = self.find_element(locator_text).text
        return accordion_text

    @allure.step('Нажать на кнопку "Заказать"')
    def click_to_button_order(self, button_order):
        button = self.visibility_of_element_located(button_order)
        button.click()

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_on_logo_yandex(self):
        self.visibility_of_element_located(MainPageLocators.LOCATOR_LOGO_YANDEX).click()

    @allure.step('Проверить переход на страницу Яндекс Дзен')
    def check_to_yandex_page(self, index_page):
        self.switch_to_window(index_page)
        self.presence_of_element_located(MainPageLocators.LOCATOR_BUTTON_YANDEX_SEARCH)
        return self.get_current_url()

    @allure.step('Кликнуть по логотипу "Самокат')
    def click_on_logo_scooter(self):
        self.visibility_of_element_located(MainPageLocators.LOCATOR_LOGO_SCOOTER).click()

    @allure.step('Проверить главный заголовок')
    def check_scooter(self):
        return self.visibility_of_element_located(MainPageLocators.LOCATOR_SCOOTER)
