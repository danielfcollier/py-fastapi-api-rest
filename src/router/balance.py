from src.lib.db import Db

def get(id):
    return Db.read(id)
