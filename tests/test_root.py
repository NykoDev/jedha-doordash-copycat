import requests

def test_root():
    response = requests.get("http://localhost:8080/")
    assert response.status_code == 200
    assert "message" in response.json()
