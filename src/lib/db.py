import os
import json

from src.lib.file_handler import *

DB_PATH = os.path.join("src", "db", "data.json")

class Db():
  @staticmethod
  def read_all():
    data = read_json(DB_PATH)

    return data

  @staticmethod
  def reset():
    write_json(DB_PATH, json.dumps([]))

    return Db.read_all()

  @staticmethod
  def create(account):
    data = Db.read_all()
    data.append(account)
    write_json(DB_PATH, json.dumps(data))

    return account

  @staticmethod
  def read(id):
    data = Db.read_all()
    for element in data:
      if (element["id"] == id):
        return element

    return None

  @staticmethod
  def increment(account, amount):
    return Db.update(account, amount)

  @staticmethod
  def decrement(account, amount):
    return Db.update(account, -amount)

  @staticmethod
  def update(account, amount):
    data = Db.read_all()

    for index, element in enumerate(data):
      if element["id"] == account["id"]:
        new_amount = element["balance"] + amount
        data[index]["balance"] = new_amount
        write_json(DB_PATH, json.dumps(data))

        return { "id": account["id"], "balance": new_amount }
