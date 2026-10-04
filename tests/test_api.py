import requests

BASE_URL = "http://127.0.0.1:8000"


def test_get_account():
    response = requests.get(f"{BASE_URL}/accounts/1001")

    assert response.status_code == 200
    assert response.json()["name"] == "John"


def test_invalid_account():
    response = requests.get(f"{BASE_URL}/accounts/9999")

    assert response.status_code == 404


def test_successful_transfer():
    response = requests.post(
        f"{BASE_URL}/transfer",
        params={
            "sender": "1001",
            "receiver": "1002",
            "amount": 1000
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "SUCCESS"


def test_insufficient_balance():
    response = requests.post(
        f"{BASE_URL}/transfer",
        params={
            "sender": "1002",
            "receiver": "1001",
            "amount": 100000
        }
    )

    assert response.status_code == 400