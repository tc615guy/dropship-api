from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..schemas import ApproveRequest
from ..models import Product

router = APIRouter(
    prefix="/approve",
    tags=["approve"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def approve(req: ApproveRequest, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == req.id).first()
    if not product:
        return {"ok": False, "error": "Product not found"}
    return {"ok": True, "approved_id": product.id}
