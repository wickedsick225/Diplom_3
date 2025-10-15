from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст '{text}' в поле")
    def type_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    def is_not_visible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.get_element(source_locator)
        target = self.get_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
