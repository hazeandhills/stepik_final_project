from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-primary")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > div:nth-of-type(1) > .alertinner")
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group a.btn")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
