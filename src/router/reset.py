from src.lib.db import Db

def post():
  Db.reset()

  return "OK"
