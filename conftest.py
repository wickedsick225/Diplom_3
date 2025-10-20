import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from pages.order_feed_page import OrderFeedPage
from urls import URLS
from helpers import create_user_api, delete_user_api


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Unknown browser: {browser}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(driver):
    with allure.step("Создаём и авторизуем пользователя через API и UI"):
        feed_page = OrderFeedPage(driver)
        user_data, access_token = create_user_api()

        feed_page.open(URLS.BASE_URL)
        feed_page.login_ui(user_data["email"], user_data["password"])

    yield driver

    with allure.step("Удаляем пользователя через API"):
        delete_user_api(access_token)
