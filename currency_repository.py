from sqlalchemy.orm import Session

import schema.currency
from models.currency import Currency


def find_currency_by_code(db: Session, code: str):
    return db.query(Currency).filter(Currency.code == code).first()


def save_currency(db: Session, currency_schema: schema.currency.Currency):
    currency = Currency(**currency_schema.model_dump())

    db.add(currency)
    db.commit()

    db.refresh(currency)
    return currency
