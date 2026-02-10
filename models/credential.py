"""
Credential — Operator, Vendor, Host certifications.
═══════════════════════════════════════════════════════════════════════
Credentials are annual NFTs that authorize protocol roles.
Operator: run spaces, host events, manage vendor relationships.
Vendor: sell products/services within the Helios economy.
Host: host events and experiences within spaces.
"""

from datetime import datetime, timezone, timedelta
from sqlalchemy import Column, String, DateTime, Integer, Float, Boolean
from models.member import Base


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Identity ═══
    credential_id = Column(String(64), unique=True, nullable=False, index=True)
    holder_id = Column(String(64), nullable=False, index=True)

    # ═══ Type ═══
    credential_type = Column(String(20), nullable=False, index=True)  # operator, vendor, host, educator, auditor
    fee_paid_usd = Column(Float, nullable=False)

    # ═══ Validity ═══
    issued_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    expires_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True, index=True)
    renewed_count = Column(Integer, default=0)

    # ═══ Verification ═══
    verified_by = Column(String(64), nullable=True)                   # Who approved
    verification_notes = Column(String(280), nullable=True)

    def __repr__(self):
        return f"<Credential {self.credential_type} | {self.holder_id} [{'active' if self.is_active else 'expired'}]>"

    def to_dict(self):
        return {
            "credential_id": self.credential_id,
            "holder_id": self.holder_id,
            "credential_type": self.credential_type,
            "fee_paid_usd": self.fee_paid_usd,
            "is_active": self.is_active,
            "issued_at": self.issued_at.isoformat() if self.issued_at else None,
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "renewed_count": self.renewed_count,
        }

    @property
    def is_expired(self):
        return datetime.now(timezone.utc) > self.expires_at

    def check_and_deactivate(self):
        """Deactivate if expired."""
        if self.is_expired and self.is_active:
            self.is_active = False
            return True
        return False
