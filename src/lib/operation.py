from db import Db

class Operation():
  @staticmethod
  def handler(data):
    match data["type"]:

      case "deposit":
        return Operation._deposit(data)

      case "transfer":
        return Operation._transfer(data)

      case "withdraw":
        return Operation._withdraw(data)

  @staticmethod
  def _deposit(data):
    id = data["destination"]
    account = Db.read(id)
    if account is None:
      new_account = dict(
        id = id,
        balance = data["amount"]
      )
      Db.create(new_account)

      return dict(destination = new_account)

    updated_account = Db.increment(account, data["amount"])

    return dict(destination = updated_account)

  @staticmethod
  def _transfer(data):
    origin = Operation._withdraw(data)
    if origin is not None:
      destination = Operation._deposit(data)

      return dict(origin = origin["origin"], destination = destination["destination"])

  @staticmethod
  def _withdraw(data):
    id = data["origin"]
    account = Db.read(id)
    updated_account = Db.decrement(account, data["amount"])

    return dict(origin = updated_account)
