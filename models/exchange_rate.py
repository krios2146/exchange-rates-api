from sqlalchemy import DECIMAL, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.currency import Currency


class ExchangeRate(Base):
    __tablename__ = "exchange_rates"
    __table_args__ = UniqueConstraint("base_currency", "target_currency")

    id: Mapped[int] = mapped_column(primary_key=True)
    base_currency: Mapped["Currency"] = relationship(back_populates="id")
    target_currency: Mapped["Currency"] = relationship(back_populates="id")
    rate: Mapped[DECIMAL] = mapped_column()
