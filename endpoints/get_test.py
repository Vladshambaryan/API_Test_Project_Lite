import requests
import allure


BASE_URL = "http://167.172.172.115:52355"


def get_meme(authorize, new_mem_id):
    """Тест на получение мема по ID (GET запрос)."""
    response = requests.get(f"{BASE_URL}/meme/{new_mem_id}", headers=authorize)
    # print(response.text)
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Failed to get meme"
        data = response.json()
    with allure.step("Checking response id ."):
        assert data['id'] == new_mem_id, "Meme ID does not match"
