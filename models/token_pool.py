"""Token Pool model — locked pools, verifiable balances."""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float
from models.member import Base


class TokenPool(Base):
    __tablename__ = "token_pools"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    initial_amount = Column(Float, nullable=False)
    status = Column(String(20), default="locked")
    unlock_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<TokenPool {self.name} | {self.amount:,.2f} HLS>"
