import requests

def test_calculate_fee():
    payload = {"distance_km": 5.0, "weight_kg": 2.0}
    response = requests.post("http://localhost:8080/calculate-fee/", json=payload)
    assert response.status_code == 200
    assert "fee" in response.json()

def test_calculate_fee_invalid_distance():
    payload = {"distance_km": "not_a_number", "weight_kg": 2.0}
    response = requests.post("http://localhost:8080/calculate-fee/", json=payload)
    assert response.status_code == 422

def test_calculate_fee_invalid_weight():
    payload = {"distance_km": 5.0, "weight_kg": "not_a_number"}
    response = requests.post("http://localhost:8080/calculate-fee/", json=payload)
    assert response.status_code == 422

def test_calculate_fee_missing_field():
    payload = {"distance_km": 5.0}  # weight_kg manquant
    response = requests.post("http://localhost:8080/calculate-fee/", json=payload)
    assert response.status_code == 422

def test_calculate_fee_empty_body():
    response = requests.post("http://localhost:8080/calculate-fee/", json={})
    assert response.status_code == 422
