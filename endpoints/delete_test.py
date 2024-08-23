import requests
import allure


BASE_URL = "http://167.172.172.115:52355"

def delete_meme(authorize, new_mem_id):
    """Тест на удаление мема (DELETE запрос)."""
    response = requests.delete(f"{BASE_URL}/meme/{new_mem_id}", headers=authorize)
    # print(response.text)
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Meme deletion failed"
