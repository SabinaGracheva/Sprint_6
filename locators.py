from selenium.webdriver.common.by import By


class MainPageLocators:
    LOCATOR_ACCORDION_BUTTON_1 = (By.ID, 'accordion__heading-0')
    LOCATOR_ACCORDION_TEXT_1 = (By.ID, 'accordion__panel-0')
    LOCATOR_ACCORDION_BUTTON_2 = (By.ID, 'accordion__heading-1')
    LOCATOR_ACCORDION_TEXT_2 = (By.ID, 'accordion__panel-1')
    LOCATOR_ACCORDION_BUTTON_3 = (By.ID, 'accordion__heading-2')
    LOCATOR_ACCORDION_TEXT_3 = (By.ID, 'accordion__panel-2')
    LOCATOR_ACCORDION_BUTTON_4 = (By.ID, 'accordion__heading-3')
    LOCATOR_ACCORDION_TEXT_4 = (By.ID, 'accordion__panel-3')
    LOCATOR_ACCORDION_BUTTON_5 = (By.ID, 'accordion__heading-4')
    LOCATOR_ACCORDION_TEXT_5 = (By.ID, 'accordion__panel-4')
    LOCATOR_ACCORDION_BUTTON_6 = (By.ID, 'accordion__heading-5')
    LOCATOR_ACCORDION_TEXT_6 = (By.ID, 'accordion__panel-5')
    LOCATOR_ACCORDION_BUTTON_7 = (By.ID, 'accordion__heading-6')
    LOCATOR_ACCORDION_TEXT_7 = (By.ID, 'accordion__panel-6')
    LOCATOR_ACCORDION_BUTTON_8 = (By.ID, 'accordion__heading-7')
    LOCATOR_ACCORDION_TEXT_8 = (By.ID, 'accordion__panel-7')
    LOCATOR_BUTTON_ORDER_UP = (By.CSS_SELECTOR, ".Header_Nav__AGCXC .Button_Button__ra12g:first-child")
    LOCATOR_BUTTON_ORDER_DOWN = (By.XPATH, '//button[contains(@class, "Button_Middle")]')
    LOCATOR_LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru"]')
    LOCATOR_BUTTON_YANDEX_SEARCH = (By.XPATH, '//button[@class="dzen-search-arrow-common__button"]')
    LOCATOR_LOGO_SCOOTER = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    LOCATOR_SCOOTER = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')


class OrderPageLocators:
    LOCATOR_NAME = (By.XPATH, '//input[contains(@placeholder, "* Имя")]')
    LOCATOR_SURNAME = (By.XPATH, '//input[contains(@placeholder, "* Фамилия")]')
    LOCATOR_ADDRESS = (By.XPATH, '//input[contains(@placeholder, "* Адрес: куда привезти заказ")]')
    LOCATOR_METRO = (By.XPATH, '//input[contains(@placeholder, "* Станция метро")]')
    LOCATOR_METRO_STATION = (By.XPATH, '//div[@class="select-search__select"]')
    LOCATOR_PHONE = (By.XPATH, '//input[contains(@placeholder, "* Телефон: на него позвонит курьер")]')
    LOCATOR_BUTTON_NEXT = (By.XPATH, '//button[contains(@class, "Button_Middle")]')
    LOCATOR_WHEN_TO_BRING = (By.XPATH, '//input[contains(@placeholder, "* Когда привезти самокат")]')
    LOCATOR_WHEN_TO_BRING_DAY = (By.XPATH, '//div[@aria-label="Choose суббота, 4-е ноября 2023 г."]')
    LOCATOR_RENTAL_PERIOD = (By.XPATH, '//div[@class="Dropdown-control"]')
    LOCATOR_RENTAL_PERIOD_DAY = [(By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="трое суток"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="четверо суток"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="пятеро суток"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="шестеро суток"]'),
                             (By.XPATH, '//div[@class="Dropdown-option" and text()="семеро суток"]')]
    LOCATOR_COLOR_SCOOTERS = [(By.ID, 'black'), (By.ID, 'grey')]
    LOCATOR_COMMENT = (By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]')
    LOCATOR_BUTTON_ORDER = (By.XPATH, '//button[contains(@class, "Button_Middle")][2]')
    LOCATOR_BUTTON_YES = (By.CSS_SELECTOR, '.Order_Modal__YZ-d3 .Button_Button__ra12g:first-child + .Button_Button__ra12g')
    LOCATOR_ORDER_ISSUED = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
