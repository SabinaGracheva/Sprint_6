from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def click_accordion_button(self, locator_button):
        self.find_element(locator_button).click()

    def check_accordion_text(self, locator_text):
        accordion_text = self.find_element(locator_text).text
        return accordion_text

    def click_on_logo(self):
        self.visibility_of_element_located(MainPageLocators.LOCATOR_LOGO).click()


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