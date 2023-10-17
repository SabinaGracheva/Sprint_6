from time import sleep
import pytest
from pages.main_page import MainPage, MainPageLocators


class TestMainPage:
    def test_how_much_does_it_cost(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.visibility_of_element_located(MainPageLocators.LOCATOR_HOW_MUCH_DOES_IT_COST)
        main_page.click_drop_down_list()
        element = main_page.check_element_text()
        assert element == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', \
            f'Текст-пояснение не соответствует вопросу "Сколько это стоит? И как оплатить?"'

    def test_click_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_logo()
        main_page.visibility_of_element_located()
