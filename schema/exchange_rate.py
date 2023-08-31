from _decimal import Decimal
from pydantic import BaseModel, Field

from schema.currency import Currency


class ExchangeRate(BaseModel):
    id: int
    base_currency: Field(Currency)
    target_currency: Field(Currency)
    rate: Decimal
