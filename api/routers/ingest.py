from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/ingest",
    tags=["ingest"]
)

class IngestRequest(BaseModel):
    domain: str

class IngestResponse(BaseModel):
    ok: bool
    message: str

@router.post("/", response_model=IngestResponse)
def ingest_candidate(payload: IngestRequest):
    # In the future: call your scraper or harvesting script
    # Example:
    # subprocess.run(["python", "mvp.py", "--domain", payload.domain], check=True)

    return {
        "ok": True,
        "message": f"Ingest started for {payload.domain}"
    }
