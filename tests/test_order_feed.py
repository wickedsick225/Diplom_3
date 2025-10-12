import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators import MainPageLocators
from urls import URLS


@allure.feature("Раздел 'Лента заказов'")
class TestOrderFeed:

    @allure.title("При создании заказа счётчики увеличиваются, заказ появляется в работе")
    def test_order_feed_counters_and_list(self, authorized_user):
        driver = authorized_user
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        # 1️⃣ Открываем ленту заказов и фиксируем начальные значения
        feed.open(URLS.BASE_URL + "feed")
        total_before = feed.get_total_orders()
        today_before = feed.get_today_orders()

        # 2️⃣ Возвращаемся на главную и создаём заказ
        main.open(URLS.BASE_URL)
        main.add_first_ingredient_to_order()
        main.click(MainPageLocators.set_order_btn)

        # 3️⃣ Снова открываем ленту заказов
        feed.open(URLS.BASE_URL + "feed")

        # 4️⃣ Берём новые значения
        total_after = feed.get_total_orders()
        today_after = feed.get_today_orders()

        # 5️⃣ Проверяем, что значения увеличились
        assert total_after > total_before, "Счётчик 'за всё время' не увеличился"
        assert today_after >= today_before, "Счётчик 'за сегодня' не увеличился"
        assert feed.orders_in_progress() > 0, "Нет заказов в работе"
