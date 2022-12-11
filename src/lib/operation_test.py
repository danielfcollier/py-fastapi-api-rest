from src.lib.operation import Operation

def test_handler_deposit():
  data = {
    "type": "deposit",
    "destination": 1,
    "amount": 10
  }
  expected = {
    "destination": {
      "id": 1,
      "balance": 20
    }
  }
  output = Operation.handler(data)

  assert output == expected

def test_handler_transfer():
  data = {
    "type": "transfer",
    "origin": 1,
    "destination": 2,
    "amount": 10
  }
  expected = {
    "origin": {
      "id": 1,
      "balance": 10
    },
    "destination": {
      "id": 2,
      "balance": 10
    }
  }
  output = Operation.handler(data)

  assert output == expected

def test_handler_withdraw():
  data = {
    "type": "withdraw",
    "origin": 2,
    "amount": 10
  }
  expected = {
    "origin": {
      "id": 2,
      "balance": 0
    }
  }

  output = Operation.handler(data)

  assert output == expected
