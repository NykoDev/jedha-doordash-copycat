import requests

def test_status():
    response = requests.get("http://localhost:8080/status/")
    assert response.status_code == 200
    assert "status" in response.json()
