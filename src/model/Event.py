from pydantic import BaseModel

class Request(BaseModel):
  type: str
  amount: int
  origin: str | None = None
  destination: str | None = None
