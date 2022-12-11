from db import Db
from file_handler import *

def test_before():
  Db.reset()

def test_read_all():
  output = Db.read_all()
  expected = []

  assert output == expected

def test_reset():
  output = Db.reset()
  expected = []

  assert output == expected

def test_create_and_read():
  account = {
    "id": 1,
    "balance": 10
  }
  output = Db.create(account)
  expected = Db.read(account["id"])

  assert output == expected

def test_increment():
  account = Db.read(id = 1)
  increment = 1
  output = Db.increment(account, increment)
  expected = {
    "id": account["id"],
    "balance": account["balance"] + increment
  }

  assert output == expected

def test_decrement():
  account = Db.read(id = 1)
  decrement = 1
  output = Db.decrement(account, decrement)
  expected = {
    "id": account["id"],
    "balance": account["balance"] - decrement
  }

  assert output == expected
