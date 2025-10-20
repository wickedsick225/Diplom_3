import requests
import allure
from urls import URLS
from data import generate_user


@allure.step("Создаём пользователя через API")
def create_user_api():
    user_data = generate_user()
    response = requests.post(URLS.CREATE_USER, json=user_data)
    response.raise_for_status()
    access_token = response.json().get("accessToken")
    return user_data, access_token


@allure.step("Удаляем пользователя через API")
def delete_user_api(access_token):
    if not access_token:
        return
    token = access_token if access_token.startswith("Bearer ") else f"Bearer {access_token}"
    headers = {"Authorization": token}
    requests.delete(URLS.DELETE_USER, headers=headers)
