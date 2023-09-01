from sqlalchemy.orm import Session

import schema.currency
from models.currency import Currency


def find_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Currency).offset(skip).limit(limit).all()


def find_by_code(db: Session, code: str):
    return db.query(Currency).filter(Currency.code == code).first()


def save(db: Session, currency_schema: schema.currency.CurrencyAdd):
    currency = Currency(**currency_schema.model_dump())

    db.add(currency)
    db.commit()

    db.refresh(currency)
    return currency
