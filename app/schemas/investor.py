from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID

class InvestorBase(BaseModel):
    slug: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    headline: Optional[str] = None
    position: Optional[str] = None
    firm: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    crunchbase: Optional[str] = None
    angellist: Optional[str] = None
    min_investment: Optional[int] = None
    max_investment: Optional[int] = None
    target_investment: Optional[int] = None
    image: Optional[str] = None
    created_at: Optional[datetime] = None

class InvestorRead(InvestorBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
