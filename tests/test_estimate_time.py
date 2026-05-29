import requests

def test_estimate_time():
    response = requests.get("http://localhost:8080/estimate-time/10")
    assert response.status_code == 200
    assert "time" in response.json()

def test_estimate_time_invalid_input():
    response = requests.get("http://localhost:8080/estimate-time/not_a_number")
    assert response.status_code == 422

def test_estimate_time_negative_distance():
    response = requests.get("http://localhost:8080/estimate-time/-10")
    assert response.status_code == 422


def test_estimate_time_missing_distance():
    response = requests.get("http://localhost:8080/estimate-time/")
    assert response.status_code == 404
