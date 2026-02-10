"""Wallet Transaction model — member-to-member transfers."""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float
from models.member import Base


class WalletTransaction(Base):
    __tablename__ = "wallet_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_id = Column(String(64), nullable=False, index=True)
    to_id = Column(String(64), nullable=False, index=True)
    amount = Column(Float, nullable=False)
    note = Column(String(280), nullable=True)
    status = Column(String(20), default="completed", index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<WalletTx {self.from_id} → {self.to_id} | {self.amount}>"
