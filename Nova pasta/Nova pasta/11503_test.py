import requests

def test_11502_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    assert r.status_code == 200
    assert len(r.json()) > 0
