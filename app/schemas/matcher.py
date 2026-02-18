from pydantic import BaseModel, Field
from typing import List


class MatchInvestorsRequest(BaseModel):
    startup_description: str = Field(..., min_length=20)
    top_domains: int = 5
    top_investors: int = 20
    min_domain_similarity: float = 0.25


class MatchedDomain(BaseModel):
    domain: str
    similarity: float


class MatchedInvestor(BaseModel):
    investor_id: str
    name: str | None
    slug: str
    matched_domains: List[str]
    domain_match_count: int


class MatchInvestorsResponse(BaseModel):
    matched_domains: List[MatchedDomain]
    matched_investors: List[MatchedInvestor]
