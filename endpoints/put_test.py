import requests
import allure


BASE_URL = "http://167.172.172.115:52355"

def put_meme(authorize, new_mem_id):
    """Тест на обновление мема (PUT запрос)."""
    body = {
        "id": new_mem_id,
        "text": "big shrek",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["updated", "meme"],
        "info": {"author": "Miqael"}
    }
    response = requests.put(f"{BASE_URL}/meme/{new_mem_id}", json=body, headers=authorize)
    # print(response.text)
    with allure.step("Checking that the response code is 200."):
        assert response.status_code == 200, "Meme update failed"
        data = response.json()
    with allure.step("Checking text"):
        assert data['text'] == body['text'], "Text does not match"
    with allure.step("Checking url"):
        assert data['url'] == body['url'], "URL does not match"
    with allure.step("Checking tags"):
        assert data['tags'] == body['tags'], "tags does not match"
    with allure.step("Checking info"):
        assert data['info'] == body['info'], "info does not match"
