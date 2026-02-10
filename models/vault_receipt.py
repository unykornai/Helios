"""
Metal Vault Receipt (MVR) — On-chain anchored proof of physical metal.
═══════════════════════════════════════════════════════════════════════
Each MVR is an NFT primitive representing bullion purchased from an
approved dealer (APMEX). Evidence bundles are pinned to IPFS.
XRPL memo anchoring provides tamper-proof chain of custody.

Custody States: IN_TREASURY → IN_VAULT → IN_TRANSIT → DELIVERED
"""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float, Text, JSON
from models.member import Base


class VaultReceipt(Base):
    __tablename__ = "vault_receipts"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Identity ═══
    mvr_id = Column(String(64), unique=True, nullable=False, index=True)
    policy_version = Column(String(10), default="1.0")

    # ═══ Dealer / Purchase ═══
    dealer = Column(String(40), nullable=False, default="APMEX")
    invoice_id = Column(String(64), nullable=False)
    purchase_date = Column(DateTime, nullable=False)

    # ═══ Metal Details ═══
    metal = Column(String(20), nullable=False, default="GOLD")       # GOLD, SILVER, PLATINUM, PALLADIUM
    form = Column(String(40), nullable=False)                        # bar, coin, round
    purity = Column(String(10), nullable=False, default="0.9999")    # 4-nine fine
    weight_oz = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_cost_usd = Column(Float, nullable=False)
    total_cost_usd = Column(Float, nullable=False)

    # ═══ Provenance ═══
    serials = Column(JSON, default=list)                             # List of serial numbers
    custody_status = Column(String(20), default="in_treasury", index=True)

    # ═══ Evidence Bundle (IPFS) ═══
    evidence_bundle_cid = Column(String(128), nullable=True)         # IPFS CID
    sha256_evidence_bundle = Column(String(64), nullable=True)       # SHA256 of bundle

    # ═══ Chain Anchoring (XRPL) ═══
    issuer_wallet = Column(String(64), nullable=True)
    attestation_wallet = Column(String(64), nullable=True)
    xrpl_tx_hash = Column(String(128), nullable=True, index=True)

    # ═══ Timestamps ═══
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))
    delivered_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<MVR {self.mvr_id} | {self.weight_oz}oz {self.metal} [{self.custody_status}]>"

    def to_dict(self):
        return {
            "mvr_id": self.mvr_id,
            "dealer": self.dealer,
            "invoice_id": self.invoice_id,
            "purchase_date": self.purchase_date.isoformat() if self.purchase_date else None,
            "metal": self.metal,
            "form": self.form,
            "purity": self.purity,
            "weight_oz": self.weight_oz,
            "quantity": self.quantity,
            "unit_cost_usd": self.unit_cost_usd,
            "total_cost_usd": self.total_cost_usd,
            "serials": self.serials,
            "custody_status": self.custody_status,
            "evidence_bundle_cid": self.evidence_bundle_cid,
            "sha256_evidence_bundle": self.sha256_evidence_bundle,
            "xrpl_tx_hash": self.xrpl_tx_hash,
            "policy_version": self.policy_version,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    @property
    def total_oz(self):
        """Total troy ounces across all units."""
        return self.weight_oz * self.quantity

    @property
    def is_anchored(self):
        """Whether this MVR has been anchored on XRPL."""
        return bool(self.xrpl_tx_hash)
