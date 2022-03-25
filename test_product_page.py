from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.should_be_basket_button() # проверяем есть ли кнопка добавления в корзину
    page.add_product_to_basket() # добавляем товар в корзину
    page.solve_quiz_and_get_code() # решаем выражение
    page.correct_product_added_to_basket() # верный ли продукт добавлен в корзину