from utils import request_with_retry

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_list():
    url = f"{BASE_URL}/users"
    response = request_with_retry(url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'username' in data[0]

def test_create_post():
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = request_with_retry(url, method='POST', payload=payload)
    # JSONPlaceholder retorna 201 e echo do payload
    assert response.status_code == 201
    data = response.json()
    assert data.get("title") == "foo"
    assert data.get("userId") == 1
