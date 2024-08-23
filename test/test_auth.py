from endpoints import authorization
import pytest
import allure

AUTH_URL = 'http://167.172.172.115:52355/authorize'
token = 'TiPPUbj4qRWfKQJ'

@allure.title("Send request get_token")
@pytest.mark.regression
def test_get_token():
    """Тест на получение токена."""
    authorization.get_token()


@allure.title("Send request is_token_alive")
@pytest.mark.regression
def test_is_token_alive():
    """Тест на проверку, жив ли токен."""
    authorization.is_token_alive(token)


@allure.title("Send request refresh_token")
@pytest.mark.regression
def test_refresh_token():
    """Тест на обновление токена."""
    authorization.refresh_token()
