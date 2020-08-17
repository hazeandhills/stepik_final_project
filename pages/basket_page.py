from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket.click()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are present, but should not be"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"

    def go_to_basket_page_from_product(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket.click()
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Items are present, but should not be"
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"
