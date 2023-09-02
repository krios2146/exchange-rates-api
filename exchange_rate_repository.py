from sqlalchemy.orm import Session

from models.currency import Currency
from models.exchange_rate import ExchangeRate
from schema.exchange_rate import ExchangeRateAdd


def find_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExchangeRate).offset(skip).limit(limit).all()


def save(db: Session, exchange_rate_schema: ExchangeRateAdd):
    base_currency = db.query(Currency).filter(Currency.code == exchange_rate_schema.base_currency_code).first()
    target_currency = db.query(Currency).filter(Currency.code == exchange_rate_schema.target_currency_code).first()
    exchange_rate = ExchangeRate(base_currency_id=base_currency.id,
                                 target_currency_id=target_currency.id,
                                 rate=exchange_rate_schema.rate)

    db.add(exchange_rate)
    db.commit()

    db.refresh(exchange_rate)
    return exchange_rate
