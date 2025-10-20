import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import URLS
from locators import MainPageLocators


@allure.feature("Раздел 'Лента заказов'")
class TestOrderFeed:

    @allure.title("При создании заказа счётчики увеличиваются")
    def test_order_feed_counters_increase(self, authorized_user):
        driver = authorized_user
        main = MainPage(driver)
        feed = OrderFeedPage(driver)

        with allure.step("Открываем ленту заказов и фиксируем начальные значения"):
            feed.open(URLS.FEED_URL)
            total_before = feed.get_total_orders()
            today_before = feed.get_today_orders()

        with allure.step("Создаём новый заказ"):
            main.open(URLS.BASE_URL)
            main.add_first_ingredient_to_order()
            main.click(MainPageLocators.set_order_btn)

        with allure.step("Проверяем, что счётчики увеличились"):
            feed.open(URLS.FEED_URL)
            total_after = feed.get_total_orders()
            today_after = feed.get_today_orders()
            assert total_after > total_before, "Счётчик 'всего заказов' не увеличился"
            assert today_after >= today_before, "Счётчик 'за сегодня' не увеличился"

    @allure.title("Созданный заказ появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, authorized_user):
        driver = authorized_user
        feed = OrderFeedPage(driver)
        feed.open(URLS.FEED_URL)

        with allure.step("Проверяем, что есть хотя бы один заказ в работе"):
            assert feed.orders_in_progress() > 0, "Нет заказов в разделе 'В работе'"
