import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.order_feed_page import OrderFeedPage
from locators import MainPageLocators
from urls import URLS


@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise RuntimeError("Unsupported browser in this fixture")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(driver):
    """
    Создаёт пользователя через API, логинит через UI и возвращает авторизованный драйвер.
    Возвращаем token на удаление в teardown.
    """
    order_feed = OrderFeedPage(driver)
    user_data, access_token = order_feed.create_user_api()

    # Перейти на главную
    driver.get(URLS.BASE_URL)
    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "AppHeader_header__link__3D_hX"))
    )
    wait = WebDriverWait(driver, 10)

    # открыть личный кабинет (кнопка в хедере)
    personal_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.personal_account_btn))
    # Ждём, пока исчезнет модальное окно, если оно есть
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )
    except:
        pass  # если модалки нет, просто идём дальше
    personal_btn.click()

    # ввести данные для логина и нажать Войти
    wait.until(EC.element_to_be_clickable(MainPageLocators.email_field_auth)).send_keys(user_data["email"])
    wait.until(EC.element_to_be_clickable(MainPageLocators.password_field_auth)).send_keys(user_data["password"])
    wait.until(EC.element_to_be_clickable(MainPageLocators.login_auth_btn)).click()

    # ждём признака успешной авторизации — кнопку "Оформить заказ"
    wait.until(EC.visibility_of_element_located(MainPageLocators.set_order_btn))

    yield driver

    # teardown: удалить созданного пользователя через API
    order_feed.delete_user_api(access_token)
