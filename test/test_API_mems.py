import pytest
import allure
from endpoints import post_test, get_test, get_all_test, put_test, delete_test

from .test_data import (TEST, NEGATIVE_TEST, UPDATE_TEST)

BASE_URL = "http://167.172.172.115:52355"
@allure.feature('Post')
@allure.title("Send request post mem")
@pytest.mark.regression
@pytest.mark.parametrize('data', TEST)
def test_post_meme(authorize, data):
    """Тест на создание нового мема (POST запрос)."""
    post_test.post_meme(authorize)


@allure.feature('Post')
@allure.title("Send request post negative test")
@pytest.mark.regression
@pytest.mark.parametrize('data', NEGATIVE_TEST)
def test_negative_meme(authorize, data):
    """Тест негативный на создание нового мема (POST запрос)."""
    post_test.post_meme(authorize)


@allure.feature('Get')
@allure.title("Send request get mem")
@pytest.mark.regression
def test_get_meme(authorize, new_mem_id):
    """Тест на получение мема по ID (GET запрос)."""
    get_test.get_meme(authorize, new_mem_id)


@allure.feature('Get all')
@allure.title("Send request get all mems")
@pytest.mark.regression
def test_get_all_memes(authorize):
    """Тест на получение списка всех мемов (GET запрос)."""
    get_all_test.get_all_memes(authorize)


@allure.feature('Put')
@allure.title("Send request put")
@pytest.mark.regression
@pytest.mark.parametrize('data', UPDATE_TEST)
def test_put_meme(data, authorize, new_mem_id):
    """Тест на обновление мема (PUT запрос)."""
    put_test.put_meme(authorize, new_mem_id)


@allure.feature('Put')
@allure.title("Send request put negative test")
@pytest.mark.regression
@pytest.mark.parametrize('data', NEGATIVE_TEST)
def test_negative_put_meme(data, authorize, new_mem_id):
    """Тест негативный на обновление мема (PUT запрос)."""
    put_test.put_meme(authorize, new_mem_id)


@allure.feature('Delete')
@allure.title("Send request delete")
@pytest.mark.regression
def test_delete_meme(authorize, new_mem_id):
    """Тест на удаление мема (DELETE запрос)."""
    delete_test.delete_meme(authorize, new_mem_id)
