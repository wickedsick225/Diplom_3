import requests
import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from urls import URLS
from data import generate_user


class OrderFeedPage(BasePage):

    @allure.step("Авторизуемся через UI")
    def login_ui(self, email, password):
        self.click(MainPageLocators.personal_account_btn)
        self.type_text(MainPageLocators.email_field_auth, email)
        self.type_text(MainPageLocators.password_field_auth, password)
        self.click(MainPageLocators.login_auth_btn)
        self.is_visible(MainPageLocators.set_order_btn)

    @allure.step("Получаем количество выполненных заказов за всё время")
    def get_total_orders(self):
        return int(self.get_text(MainPageLocators.total_orders))

    @allure.step("Получаем количество выполненных заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(MainPageLocators.today_orders))

    @allure.step("Проверяем наличие заказов в разделе 'В работе'")
    def orders_in_progress(self):
        return len(self.driver.find_elements(*MainPageLocators.order_items))


