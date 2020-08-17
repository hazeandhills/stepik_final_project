from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_product_to_basket()
        self.should_be_product_in_basket()
        self.price_should_be_match()

    def add_product_to_basket(self):
        product = self.browser.find_element(*ProductPageLocators.BASKET)
        product.click()

    def should_be_product_in_basket(self):
        product_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_basket == product_name, "Goods do not match"

    def price_should_be_match(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but is present"
