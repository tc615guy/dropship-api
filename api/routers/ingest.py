from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Product
from ..schemas import IngestRequest, ProductResponse

router = APIRouter(
    prefix="/ingest",
    tags=["ingest"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ProductResponse)
def ingest_candidate(payload: IngestRequest, db: Session = Depends(get_db)):
    product = Product(url=payload.domain, name=payload.domain)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
