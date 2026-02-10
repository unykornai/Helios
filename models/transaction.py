"""Transaction model — all network activity events."""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float, JSON
from models.member import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(String(64), nullable=False, index=True)
    activity_type = Column(String(30), nullable=False, index=True)
    value = Column(Float, default=1.0)
    extra_data = Column(JSON, default=dict)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Transaction {self.member_id} | {self.activity_type}>"
