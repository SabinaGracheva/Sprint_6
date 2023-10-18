import allure
import pytest
from pages.main_page import MainPage, MainPageLocators


class TestMainPage:
    @allure.title('Проверка выпадающего списка "Вопросы о важном"')
    @pytest.mark.parametrize(
        'locator_button, locator_text, text',
        [
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_1,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_1,
             "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_2,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_2,
             "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_3,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_3,
             "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_4,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_4,
             "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_5,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_5,
             "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_6,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_6,
             "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_7,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_7,
             "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
            [MainPageLocators.LOCATOR_ACCORDION_BUTTON_8,
             MainPageLocators.LOCATOR_ACCORDION_TEXT_8,
             "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
        ]
    )
    def test_how_much_does_it_cost(self, driver, locator_button, locator_text, text):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.visibility_of_element_located(locator_button)
        main_page.click_accordion_button(locator_button)
        accordion_text = main_page.check_accordion_text(locator_text)
        assert accordion_text == text

    @allure.title('Переход на Яндекс Дзен через логотип Яндекс')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_logo_yandex()
        current_url = main_page.check_to_yandex_page(1)
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Переход на главную через логотип "Самокат"')
    def test_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site('https://qa-scooter.praktikum-services.ru/')
        main_page.click_on_logo_scooter()
        assert main_page.check_scooter()
