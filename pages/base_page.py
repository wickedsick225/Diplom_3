from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    def open(self, url):
        """Открывает страницу по указанному URL"""
        self.driver.get(url)

    def click(self, locator):
        """Кликает по элементу после ожидания кликабельности"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        """Возвращает текст видимого элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        """Проверяет, что элемент виден"""
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    def is_not_visible(self, locator):
        """Проверяет, что элемент исчез"""
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True

    def get_element(self, locator):
        """Возвращает сам элемент после ожидания появления"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивает элемент (drag & drop)"""
        source = self.get_element(source_locator)
        target = self.get_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()
