import pytest
import requests


BASE_URL = "http://167.172.172.115:52355"

@pytest.fixture(scope="session")
def authorize():
    """Фикстура для авторизации и получения токена."""
    username = "vlad"
    response = requests.post(f"{BASE_URL}/authorize", json={"name": username})
    print(response.text)
    assert response.status_code == 200, "Authorization failed"
    token = response.json().get('token')
    return {'Authorization': token}


@pytest.fixture
def new_mem_id(authorize):
    """Фикстура для создания нового мема и получения его ID."""
    body = {
        "text": "Example meme",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["example", "test"],
        "info": {"author": "Test Author"}
    }
    response = requests.post(f"{BASE_URL}/meme", json=body, headers=authorize)
    print(response.text)
    assert response.status_code == 201 or 200, "Failed to create meme"
    return response.json().get('id')
