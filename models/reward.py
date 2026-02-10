"""Reward model — every payout, fully auditable."""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float
from models.member import Base


class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column(String(64), nullable=False, index=True)
    source_member_id = Column(String(64), nullable=True)
    amount = Column(Float, nullable=False)
    reward_type = Column(String(40), nullable=False, index=True)
    activity_type = Column(String(30), nullable=True)
    reason = Column(String(280), nullable=True)
    status = Column(String(20), default="settled", index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Reward {self.member_id} | {self.amount} HLS>"
