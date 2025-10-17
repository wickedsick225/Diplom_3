import allure
from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main_page(self, url):
        super().open(url)

    @allure.step("Переходим в раздел 'Конструктор'")
    def go_to_constructor(self):
        self.click(MainPageLocators.constructor_btn)
        self.is_visible(MainPageLocators.heading_main_gape)

    @allure.step("Переходим в раздел 'Лента заказов'")
    def go_to_order_feed(self):
        self.click(MainPageLocators.order_feed_btn)
        self.is_visible(MainPageLocators.heading_order_feed)

    @allure.step("Открываем всплывающее окно первого ингредиента")
    def open_first_ingredient_popup(self):
        self.click(MainPageLocators.first_ingredient)
        self.is_visible(MainPageLocators.popup_window)

    @allure.step("Закрываем всплывающее окно ингредиента")
    def close_popup(self):
        self.click(MainPageLocators.cross_btn)
        self.is_not_visible(MainPageLocators.popup_window)

    @allure.step("Добавляем первый ингредиент в заказ (drag and drop)")
    def add_first_ingredient_to_order(self):
        self.drag_and_drop(MainPageLocators.first_ingredient, MainPageLocators.order_panel)

    @allure.step("Получаем значение счётчика ингредиента")
    def get_counter_value(self):
        return self.get_text(MainPageLocators.counter_main_page)

    @allure.step("Нажимаем 'Оформить заказ'")
    def click_set_order(self):
        self.click(MainPageLocators.set_order_btn)

    @allure.step("Проверяем, что заголовок 'Соберите бургер' отображается")
    def is_constructor_heading_visible(self):
        return self.is_visible(MainPageLocators.heading_main_gape)

    @allure.step("Проверяем, что заголовок 'Лента заказов' отображается")
    def is_order_feed_heading_visible(self):
        return self.is_visible(MainPageLocators.heading_order_feed)
