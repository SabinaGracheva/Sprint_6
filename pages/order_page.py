import random
from faker import Faker
from pages.base_page import BasePage
from locators import OrderPageLocators

faker = Faker('ru_RU')


class OrderPage(BasePage):
    def input_name(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_NAME).send_keys(faker.first_name())

    def input_surname(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_SURNAME).send_keys(faker.last_name())

    def input_address(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_ADDRESS).send_keys("г. Москва, ул. Отрадная, д. 3")

    def choose_metro(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_METRO).click()
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_METRO_STATION).click()

    def input_phone(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_PHONE).send_keys(f'+7{random.randint(100000000, 999999999)}')

    def click_button_next(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_BUTTON_NEXT).click()

    def click_when_to_bring_scooter(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_WHEN_TO_BRING).click()
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_WHEN_TO_BRING_DAY).click()

    def click_rental_period(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_RENTAL_PERIOD).click()
        self.visibility_of_element_located(random.choice(OrderPageLocators.LOCATOR_RENTAL_PERIOD_DAY)).click()

    def click_color_scooter(self):
        self.visibility_of_element_located(random.choice(OrderPageLocators.LOCATOR_COLOR_SCOOTERS)).click()

    def input_comment(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_COMMENT).send_keys("Позвонить за час до доставки")

    def click_button_order(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_BUTTON_ORDER).click()

    def click_button_yes(self):
        self.visibility_of_element_located(OrderPageLocators.LOCATOR_BUTTON_YES).click()

    def check_order_issued(self):
        return self.visibility_of_element_located(OrderPageLocators.LOCATOR_ORDER_ISSUED)
