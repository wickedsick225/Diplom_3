import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Переходим в раздел 'Конструктор'")
    def go_to_constructor(self):
        self.click(MainPageLocators.constructor_btn)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.heading_main_gape))

    @allure.step("Переходим в раздел 'Лента заказов'")
    def go_to_order_feed(self):
        self.click(MainPageLocators.order_feed_btn)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.heading_order_feed))

    @allure.step("Открываем всплывающее окно первого ингредиента")
    def open_first_ingredient_popup(self):
        self.click(MainPageLocators.first_ingredient)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.popup_window))

    @allure.step("Закрываем всплывающее окно ингредиента")
    def close_popup(self):
        self.click(MainPageLocators.cross_btn)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.popup_window))

    @allure.step("Добавляем ингредиент в заказ (drag and drop)")
    def add_first_ingredient_to_order(self):
        # ждём появления ингредиента и панели заказа
        source = self.wait.until(EC.visibility_of_element_located(MainPageLocators.first_ingredient))
        target = self.wait.until(EC.visibility_of_element_located(MainPageLocators.order_panel))
        
        # небольшое движение мыши к элементу — помогает при нестабильных dnd
        ActionChains(self.driver)\
            .move_to_element(source)\
            .click_and_hold(source)\
            .pause(0.3)\
            .move_to_element(target)\
            .pause(0.3)\
            .release(target)\
            .perform()


    @allure.step("Получаем значение счётчика ингредиента")
    def get_counter_value(self):
        return self.get_text(MainPageLocators.counter_main_page)
