import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from pages.order_feed_page import OrderFeedPage
from urls import URLS


@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param  # получаем строку "chrome"
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
    feed_page = OrderFeedPage(driver)
    user_data, access_token = feed_page.create_user_api()

    feed_page.open(URLS.BASE_URL)
    feed_page.login_ui(user_data["email"], user_data["password"])

    yield driver

    feed_page.delete_user_api(access_token)
