from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.schemas.investor import InvestorRead
from app.crud import investor as crud

router = APIRouter(
    prefix="/api/v1/investors",
    tags=["investors"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[InvestorRead])
async def read_investors(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    investors = await crud.get_investors(db, skip=skip, limit=limit)
    return investors

@router.get("/{investor_id}", response_model=InvestorRead)
async def read_investor(investor_id: str, db: AsyncSession = Depends(get_db)):
    db_investor = await crud.get_investor(db, investor_id=investor_id)
    if db_investor is None:
        raise HTTPException(status_code=404, detail="Investor not found")
    return db_investor
