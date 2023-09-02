from _decimal import Decimal
from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.currency import Currency


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"
    __table_args__ = (
        UniqueConstraint("base_currency_id", "target_currency_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    base_currency_id: Mapped[int] = mapped_column(ForeignKey("currencies.id"))
    target_currency_id: Mapped[int] = mapped_column(ForeignKey("currencies.id"))
    rate: Mapped[Decimal] = mapped_column()

    base_currency: Mapped["Currency"] = relationship("Currency", foreign_keys=[base_currency_id])
    target_currency: Mapped["Currency"] = relationship("Currency", foreign_keys=[target_currency_id])
