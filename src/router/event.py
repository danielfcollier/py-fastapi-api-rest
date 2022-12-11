from src.lib.operation import Operation
from src.model import Event

def post(request: Event.Request):
  return Operation.handler(dict(request))
