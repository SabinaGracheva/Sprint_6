import allure
import pytest
from locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Оформление заказа через кнопку "Заказать"')
    @pytest.mark.parametrize('button_order',
                             [MainPageLocators.LOCATOR_BUTTON_ORDER_UP,
                              MainPageLocators.LOCATOR_BUTTON_ORDER_DOWN])
    def test_order_a_scooter(self, driver, button_order):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_to_button_order(button_order)
        order_page = OrderPage(driver)
        order_page.input_name()
        order_page.input_surname()
        order_page.input_address()
        order_page.choose_metro()
        order_page.input_phone()
        order_page.click_button_next()
        order_page.click_when_to_bring_scooter()
        order_page.click_rental_period()
        order_page.click_color_scooter()
        order_page.input_comment()
        order_page.click_button_order()
        order_page.click_button_yes()
        assert order_page.check_order_issued()
