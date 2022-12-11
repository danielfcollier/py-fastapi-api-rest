from fastapi.testclient import TestClient
from fastapi import status

from src.model import Event

from main import app

client = TestClient(app)

def test_before_tests():
  response = client.post("/reset")
  print(response)
  assert response.status_code == status.HTTP_200_OK
  assert response.text == "OK"

def test_get_balance_from_non_existing_account():
  response = client.get("/balance?account_id=1234")
  expected = { "response": "0", "status": status.HTTP_404_NOT_FOUND }

  assert response.status_code == expected["status"]
  assert response.text == expected["response"]

def test_create_account_with_initial_balance():
  request: Event.Request = { "type": "deposit", "destination": "100", "amount": 10 }
  response = client.post("/event", json = request)
  expected = {
    "response": { "destination": { "id": "100", "balance": 10 } },
    "status": status.HTTP_201_CREATED
  }

  assert response.status_code == expected["status"]
  assert response.json() == expected["response"]

def test_deposit_into_existing_account():
  request: Event.Request = { "type": "deposit", "destination": "100", "amount": 10 }
  response = client.post("/event", json = request)
  expected = {
    "response": { "destination": { "id": "100", "balance": 20 } },
    "status": status.HTTP_201_CREATED
  }

  assert response.status_code == expected["status"]
  assert response.json() == expected["response"]

def test_get_balance_from_existing_account():
  response = client.get("/balance?account_id=100")
  expected = { "response": "20", "status": status.HTTP_200_OK }

  assert response.status_code == expected["status"]
  assert response.text == expected["response"]

def test_withdraw_from_non_existing_account():
  request: Event.Request = { "type": "withdraw", "origin": "200", "amount": 10 }
  response = client.post("/event", json = request)
  expected = {
    "response": "0",
    "status": status.HTTP_404_NOT_FOUND
  }

  assert response.status_code == expected["status"]
  assert response.text == expected["response"]

def test_withdraw_from_existing_account():
  request: Event.Request = { "type": "withdraw", "origin": "100", "amount": 5 }
  response = client.post("/event", json = request)
  expected = {
    "response": { "origin": { "id": "100", "balance": 15 } },
    "status": status.HTTP_201_CREATED
  }

  assert response.status_code == expected["status"]
  assert response.json() == expected["response"]

def test_transfer_from_existing_account():
  request: Event.Request = { "type": "transfer", "origin": "100", "amount": 15, "destination": "300" }
  response = client.post("/event", json = request)
  expected = {
    "response": {
      "origin": { "id": "100", "balance": 0 },
      "destination": { "id": "300", "balance": 15 }
    },
    "status": status.HTTP_201_CREATED
  }

  assert response.status_code == expected["status"]
  assert response.json() == expected["response"]

def test_transfer_from_non_existing_account():
  request: Event.Request = { "type": "transfer", "origin": "200", "amount": 15, "destination": "300" }
  response = client.post("/event", json = request)
  expected = {
    "response": "0",
    "status": status.HTTP_404_NOT_FOUND
  }

  assert response.status_code == expected["status"]
  assert response.text == expected["response"]
