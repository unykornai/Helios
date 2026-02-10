"""
Subscription — Premium tier management.
═══════════════════════════════════════════════════════════════════════
Tiers: BASE (free after $100 entry) → PLUS ($20/mo) → PRO ($99/mo) → OPERATOR ($499/mo)
Each tier unlocks additional protocol capabilities.
"""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float, Boolean
from models.member import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Identity ═══
    subscription_id = Column(String(64), unique=True, nullable=False, index=True)
    member_id = Column(String(64), nullable=False, index=True)

    # ═══ Tier ═══
    tier = Column(String(20), nullable=False, default="base", index=True)  # base, plus, pro, operator
    monthly_fee_usd = Column(Float, default=0.0)

    # ═══ Billing ═══
    is_active = Column(Boolean, default=True, index=True)
    billing_cycle_day = Column(Integer, default=1)                   # Day of month for billing
    total_paid_usd = Column(Float, default=0.0)
    months_active = Column(Integer, default=0)

    # ═══ Features Unlocked ═══
    vault_access = Column(Boolean, default=False)                    # Plus+
    space_access = Column(Boolean, default=False)                    # Pro+
    credential_access = Column(Boolean, default=False)               # Pro+
    operator_tools = Column(Boolean, default=False)                  # Operator only

    # ═══ Timestamps ═══
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    expires_at = Column(DateTime, nullable=True)
    cancelled_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Subscription {self.member_id} | {self.tier} [{'active' if self.is_active else 'inactive'}]>"

    def to_dict(self):
        return {
            "subscription_id": self.subscription_id,
            "member_id": self.member_id,
            "tier": self.tier,
            "monthly_fee_usd": self.monthly_fee_usd,
            "is_active": self.is_active,
            "vault_access": self.vault_access,
            "space_access": self.space_access,
            "credential_access": self.credential_access,
            "operator_tools": self.operator_tools,
            "months_active": self.months_active,
            "started_at": self.started_at.isoformat() if self.started_at else None,
        }

    @property
    def tier_features(self):
        """Return features unlocked by current tier."""
        features = ["network_access", "energy_flow", "ask_helios"]
        if self.vault_access:
            features.extend(["vault_dashboard", "metal_tracking", "certificate_minting"])
        if self.space_access:
            features.extend(["space_entry", "event_hosting", "room_creation"])
        if self.credential_access:
            features.extend(["credential_application", "vendor_access"])
        if self.operator_tools:
            features.extend(["operator_dashboard", "space_management", "metrics_access"])
        return features
