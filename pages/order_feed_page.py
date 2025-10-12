# pages/order_feed_page.py
import requests
import allure
from pages.base_page import BasePage
from locators import MainPageLocators
from urls import URLS
from data import generate_user


class OrderFeedPage(BasePage):

    @allure.step("Получаем количество выполненных заказов за всё время")
    def get_total_orders(self):
        return int(self.get_text(MainPageLocators.total_orders))

    @allure.step("Получаем количество выполненных заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(MainPageLocators.today_orders))

    @allure.step("Проверяем наличие заказов в разделе 'В работе'")
    def orders_in_progress(self):
        return len(self.driver.find_elements(*MainPageLocators.order_items))

    @staticmethod
    def create_user_api():
        """Создаёт пользователя через API и возвращает user_data и токен (accessToken)."""
        user_data = generate_user()
        response = requests.post(URLS.CREATE_USER, json=user_data)
        response.raise_for_status()
        # API обычно возвращает accessToken — может быть с префиксом "Bearer "
        access_token = response.json().get("accessToken")
        return user_data, access_token

    @staticmethod
    def delete_user_api(access_token):
        """Удаляет пользователя через API. Приводит токен к виду 'Bearer ...' если нужно."""
        if not access_token:
            return
        token = access_token
        # Если токен не содержит 'Bearer ' — добавим его
        if not token.strip().lower().startswith("bearer "):
            token = f"Bearer {token}"
        headers = {"Authorization": token}
        requests.delete(URLS.DELETE_USER, headers=headers)
