from src.lib.db import Db

class Operation():
  @staticmethod
  def handler(request):
    match request["type"]:

      case "deposit":
        return Operation._deposit(request)

      case "transfer":
        return Operation._transfer(request)

      case "withdraw":
        return Operation._withdraw(request)

  @staticmethod
  def _deposit(request):
    print("Deposit handler called!")
    id = request["destination"]
    account = Db.read(id)
    if account is None:
      new_account = {
        "id": id,
        "balance": request["amount"]
      }
      Db.create(new_account)

      return { "destination": new_account }

    updated_account = Db.increment(account, request["amount"])

    return { "destination": updated_account }

  @staticmethod
  def _transfer(request):
    origin = Operation._withdraw(request)
    if origin is not None:
      destination = Operation._deposit(request)

      return { "origin": origin["origin"], "destination": destination["destination"] }

  @staticmethod
  def _withdraw(request):
    id = request["origin"]
    account = Db.read(id)
    updated_account = Db.decrement(account, request["amount"])

    return { "origin": updated_account }
