from pydantic import BaseModel, constr


class Currency(BaseModel):
    id: int
    code: constr(min_length=3, max_length=3)
    full_name: str
    sign: str
