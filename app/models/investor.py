from sqlalchemy import Column, String, Integer, Text, TIMESTAMP, Float, Uuid
from app.models.base import Base
import uuid

class Investor(Base):
    __tablename__ = "investors"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug = Column(Text, nullable=True)
    name = Column(Text, nullable=True)
    first_name = Column(Text, nullable=True)
    last_name = Column(Text, nullable=True)
    headline = Column(Text, nullable=True)
    position = Column(Text, nullable=True)
    firm = Column(Text, nullable=True)
    location = Column(Text, nullable=True)
    linkedin = Column(Text, nullable=True)
    twitter = Column(Text, nullable=True)
    crunchbase = Column(Text, nullable=True)
    angellist = Column(Text, nullable=True)
    min_investment = Column(Integer, nullable=True)
    max_investment = Column(Integer, nullable=True)
    target_investment = Column(Integer, nullable=True)
    image = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"<Investor(id={self.id}, name={self.name})>"
