def approve_candidate(candidate_id: int, session: Session = Depends(get_session)):
    candidate = session.get(Candidate, candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    supplier = find_supplier_for_candidate(candidate)
    candidate.approved = True
    session.add(candidate)
    session.commit()
    session.refresh(candidate)

    return {"candidate": candidate, "supplier": supplier}
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
