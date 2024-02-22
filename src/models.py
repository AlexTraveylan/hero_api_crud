"""Module with the models of the application"""

from enum import StrEnum, auto

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Its seams that this class is not used,
    but it is used by sqlalchemy to create the models"""

    ...


class Hero(Base):
    """Hero model of sqlalchemy ORM"""

    __tablename__ = "hero"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    classe: Mapped[str] = mapped_column(String(30))
    level: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Hero(id={self.id_}, name={self.name}, classe={self.classe}, level={self.level})"


class Classe(StrEnum):
    """Enum of hero classes"""

    GUERRIER = auto()
    MAGE = auto()
    VOLEUR = auto()
    PRETRE = auto()
