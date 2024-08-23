import requests
import allure


BASE_URL = "http://167.172.172.115:52355"


def get_all_memes(authorize):
    """Тест на получение списка всех мемов (GET запрос)."""
    response = requests.get(f"{BASE_URL}/meme", headers=authorize)
    # print(response.text)
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Failed to get all memes"
        data = response.json()
        assert len(data) > 0, "Meme list is empty"
