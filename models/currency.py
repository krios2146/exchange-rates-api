from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(3), unique=True)
    full_name: Mapped[str] = mapped_column()
    sign: Mapped[str] = mapped_column()
