from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPageLocators:
    LOCATOR_HOW_MUCH_DOES_IT_COST = (By.XPATH, '//div[@id="accordion__heading-0"]')
    LOCATOR_HOW_MUCH_DOES_IT_COST_TEXT = (By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')
    LOCATOR_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')


class MainPage(BasePage):
    def click_drop_down_list(self):
        self.find_element(MainPageLocators.LOCATOR_HOW_MUCH_DOES_IT_COST).click()

    def check_element_text(self):
        return self.find_element(MainPageLocators.LOCATOR_HOW_MUCH_DOES_IT_COST_TEXT).text

    def click_on_logo(self):
        self.visibility_of_element_located(MainPageLocators.LOCATOR_LOGO).click()

    def check_

#
# class MainPageLocators:    # Сколько это стоит? И как оплатить?
#     ACCORDIAN_TITLE_0 = (By.ID, "accordion__heading-0")
#     ACCORDIAN_CONTENT_0 = (By.ID, "accordion__panel-0")
#     # Хочу сразу несколько самокатов! Так можно?    ACCORDIAN_TITLE_1 = (By.ID, "accordion__heading-1")
#     ACCORDIAN_CONTENT_1 = (By.ID, "accordion__panel-1")    # Как рассчитывается время аренды?
#     ACCORDIAN_TITLE_2 = (By.ID, "accordion__heading-2")    ACCORDIAN_CONTENT_2 = (By.ID, "accordion__panel-2")
#     # Можно ли заказать самокат прямо на сегодня?    ACCORDIAN_TITLE_3 = (By.ID, "accordion__heading-3")
#     ACCORDIAN_CONTENT_3 = (By.ID, "accordion__panel-3")    # Можно ли продлить заказ или вернуть самокат раньше?
#     ACCORDIAN_TITLE_4 = (By.ID, "accordion__heading-4")    ACCORDIAN_CONTENT_4 = (By.ID, "accordion__panel-4")
#     # Вы привозите зарядку вместе с самокатом?    ACCORDIAN_TITLE_5 = (By.ID, "accordion__heading-5")
#     ACCORDIAN_CONTENT_5 = (By.ID, "accordion__panel-5")    # Можно ли отменить заказ?
#     ACCORDIAN_TITLE_6 = (By.ID, "accordion__heading-6")    ACCORDIAN_CONTENT_6 = (By.ID, "accordion__panel-6")
#     # Я живу за МКАДом, привезёте?    ACCORDIAN_TITLE_7 = (By.ID, "accordion__heading-7")
#     ACCORDIAN_CONTENT_7 = (By.ID, "accordion__panel-7")
#     ACCORDIAN_TITLE_LIST = (By.XPATH, "//div[@class='accordion__button']")    ACCORDIAN_CONTENT_LIST = (By.XPATH, "//div[@class='accordion__panel']")