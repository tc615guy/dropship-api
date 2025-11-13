from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Product
from ..schemas import ProductResponse

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[ProductResponse])
def get_candidates(limit: int = 25, db: Session = Depends(get_db)):
    rows = db.query(Product).order_by(
        Product.reviews.desc(),
        Product.rating.desc()
    ).limit(limit).all()
    return rows
