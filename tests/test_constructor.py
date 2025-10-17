import allure
from pages.main_page import MainPage
from urls import URLS


@allure.feature("Главная страница — Конструктор")
class TestConstructor:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page(URLS.BASE_URL)
        page.go_to_order_feed()
        page.go_to_constructor()
        assert page.is_constructor_heading_visible()

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page(URLS.BASE_URL)
        page.go_to_order_feed()
        assert page.is_order_feed_heading_visible()

    @allure.title("Открытие и закрытие всплывающего окна ингредиента")
    def test_ingredient_popup_open_and_close(self, driver):
        page = MainPage(driver)
        page.open_main_page(URLS.BASE_URL)
        page.open_first_ingredient_popup()
        page.close_popup()

    @allure.title("Добавление ингредиента увеличивает счётчик")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open_main_page(URLS.BASE_URL)
        before = page.get_counter_value()
        page.add_first_ingredient_to_order()
        after = page.get_counter_value()
        assert before != after, f"Счётчик не изменился: было {before}, стало {after}"
