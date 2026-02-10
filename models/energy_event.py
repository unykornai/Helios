"""
Energy Event — Immutable ledger of all energy movements.
═══════════════════════════════════════════════════════════════════════
Every energy flow is recorded. Conservation law: total IN = total OUT.
Types: ENERGY_IN, ENERGY_ROUTE, ENERGY_STORE, ENERGY_POOL,
       ENERGY_BURN, ENERGY_REDEEM, ENERGY_CANCEL
"""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float, JSON
from models.member import Base


class EnergyEvent(Base):
    __tablename__ = "energy_events"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Event Identity ═══
    event_id = Column(String(64), unique=True, nullable=False, index=True)
    event_type = Column(String(20), nullable=False, index=True)      # ENERGY_IN, ENERGY_ROUTE, etc.

    # ═══ Parties ═══
    from_id = Column(String(64), nullable=True, index=True)          # Source (null for ENERGY_IN from entry)
    to_id = Column(String(64), nullable=True, index=True)            # Destination (null for ENERGY_BURN)

    # ═══ Amount ═══
    amount_he = Column(Float, nullable=False)                        # Energy in HE units
    amount_usd = Column(Float, nullable=True)                        # USD equivalent (if applicable)

    # ═══ Context ═══
    hop_number = Column(Integer, nullable=True)                      # For ENERGY_ROUTE — which hop
    certificate_id = Column(String(64), nullable=True, index=True)   # For STORE/REDEEM/CANCEL
    pool_name = Column(String(40), nullable=True)                    # For ENERGY_POOL — which pool

    # ═══ Metadata ═══
    reference_id = Column(String(64), nullable=True)                 # Links to triggering event
    extra_data = Column(JSON, default=dict)

    # ═══ Timestamp ═══
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Energy {self.event_type} | {self.amount_he} HE | {self.from_id}→{self.to_id}>"

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "from_id": self.from_id,
            "to_id": self.to_id,
            "amount_he": self.amount_he,
            "amount_usd": self.amount_usd,
            "hop_number": self.hop_number,
            "certificate_id": self.certificate_id,
            "pool_name": self.pool_name,
            "reference_id": self.reference_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
