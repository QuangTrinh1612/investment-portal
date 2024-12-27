from fastapi import APIRouter, Depends

from backend.app.models import StockPrice
from backend.app.api.deps import SessionDep

router = APIRouter(prefix="/stock", tags=["items"])

@router.get("/{ticker}/price", response_model=StockPrice)
async def get_stock_price(session: SessionDep, ticker: str):
    pass