from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BUTTON), "No basket button"
        
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        
    def correct_product_added_to_basket(self):
        alert = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ALERT)
        assert alert, "The product was not added to the basket"
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name_in_alert.text in alert.text, "A product with a different name has been added to the basket"