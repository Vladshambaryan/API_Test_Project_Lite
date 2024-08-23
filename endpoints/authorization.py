import requests
import allure


AUTH_URL = 'http://167.172.172.115:52355/authorize'
token = 'TiPPUbj4qRWfKQJ'

def get_token():
    """Тест на получение токена."""
    username = "vlad"
    response = requests.post(AUTH_URL, json={"name": username})
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Failed to authorize"
        token = response.json().get('token')
    with allure.step("Checking token is not None."):
        assert token is not None, "Token is None"
        # print(f"Token received: {token}")


def is_token_alive(token):
    """Тест на проверку жив ли токен."""
    response = requests.get(f'{AUTH_URL}/{token}')
    response = response
    with allure.step("Checking that the response code is 200."):
        # print(f"Token received: {token}")
        return response.status_code == 200


def refresh_token():
    """Тест на обновление токена."""
    username = "vlad"
    response = requests.post(AUTH_URL, json={"name": username})
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Failed to authorize"
        token = response.json().get('token')
    with allure.step("Checking token is not None."):
        assert token is not None, "Token is None"
        # print(f"Token received: {token}")
