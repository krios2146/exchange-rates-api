from pydantic import BaseModel, constr


class CurrencyBase(BaseModel):
    code: constr(min_length=3, max_length=3)
    full_name: str
    sign: str


class Currency(CurrencyBase):
    id: int

    class Config:
        from_attributes = True


class CurrencyAdd(CurrencyBase):
    pass
