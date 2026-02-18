from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.investor import Investor

async def get_investors(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 100
) -> List[Investor]:
    query = select(Investor).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_investor(db: AsyncSession, investor_id: str) -> Optional[Investor]:
    query = select(Investor).where(Investor.id == investor_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()
