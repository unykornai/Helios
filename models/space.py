"""
Space — Rooms, Events, Access Keys.
═══════════════════════════════════════════════════════════════════════
Spaces are containers for community activity. Each space can have rooms
(channels) and host events (ticketed or free). Access is gated by
Space Key NFTs.
"""

from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer, Float, Boolean, Text, JSON
from models.member import Base


class Space(Base):
    __tablename__ = "spaces"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Identity ═══
    space_id = Column(String(64), unique=True, nullable=False, index=True)
    name = Column(String(64), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(String(64), nullable=False, index=True)        # Must hold operator credential

    # ═══ Configuration ═══
    is_public = Column(Boolean, default=True)
    max_members = Column(Integer, default=500)
    room_count = Column(Integer, default=0)

    # ═══ Economics ═══
    entry_fee_usd = Column(Float, default=0.0)                       # 0 = free space
    total_revenue_usd = Column(Float, default=0.0)

    # ═══ Status ═══
    is_active = Column(Boolean, default=True, index=True)
    member_count = Column(Integer, default=0)

    # ═══ Timestamps ═══
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Space {self.name} | {self.member_count} members>"

    def to_dict(self):
        return {
            "space_id": self.space_id,
            "name": self.name,
            "description": self.description,
            "owner_id": self.owner_id,
            "is_public": self.is_public,
            "max_members": self.max_members,
            "room_count": self.room_count,
            "entry_fee_usd": self.entry_fee_usd,
            "member_count": self.member_count,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class SpaceEvent(Base):
    __tablename__ = "space_events"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # ═══ Identity ═══
    event_id = Column(String(64), unique=True, nullable=False, index=True)
    space_id = Column(String(64), nullable=False, index=True)
    host_id = Column(String(64), nullable=False, index=True)

    # ═══ Details ═══
    title = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    event_type = Column(String(30), default="general")               # general, workshop, summit

    # ═══ Economics ═══
    ticket_price_usd = Column(Float, default=0.0)
    max_attendees = Column(Integer, default=100)
    attendee_count = Column(Integer, default=0)
    total_revenue_usd = Column(Float, default=0.0)

    # ═══ Schedule ═══
    starts_at = Column(DateTime, nullable=True)
    ends_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    # ═══ Timestamps ═══
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Event {self.title} | ${self.ticket_price_usd}>"

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "space_id": self.space_id,
            "host_id": self.host_id,
            "title": self.title,
            "description": self.description,
            "event_type": self.event_type,
            "ticket_price_usd": self.ticket_price_usd,
            "max_attendees": self.max_attendees,
            "attendee_count": self.attendee_count,
            "starts_at": self.starts_at.isoformat() if self.starts_at else None,
            "ends_at": self.ends_at.isoformat() if self.ends_at else None,
            "is_active": self.is_active,
        }
