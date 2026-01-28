from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from typing import Optional

class Doktor(Base):
    __tablename__ = "doktor"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[Optional[str]] = mapped_column(String(13), nullable=True)


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(nullable=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doktor.id"))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patent.id"))