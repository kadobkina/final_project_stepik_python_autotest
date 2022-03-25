from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('promoN', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9", ])
def test_guest_can_add_product_to_basket(browser, promoN):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promoN}"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_be_basket_button() # проверяем есть ли кнопка добавления в корзину
    page.add_product_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # решаем выражение
    page.should_be_success_message() # товар добавлен в корзину
    page.should_be_correct_product_in_basket() # верный товар в корзине
    page.should_be_correct_price_in_basket() # цена товара совпадает с ценой в корзине