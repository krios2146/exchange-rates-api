from _decimal import Decimal
from pydantic import BaseModel, Field, constr

from schema.currency import Currency


class ExchangeRateBase(BaseModel):
    base_currency: Field(Currency)
    target_currency: Field(Currency)
    rate: Decimal

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class ExchangeRate(ExchangeRateBase):
    id: int


class ExchangeRateAdd(BaseModel):
    base_currency_code: constr(min_length=3, max_length=3)
    target_currency_code: constr(min_length=3, max_length=3)
    rate: Decimal
