from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    joining_date: Mapped[date] = mapped_column(nullable=False)
    is_registered: Mapped[bool] = mapped_column(default=False, nullable=False)
