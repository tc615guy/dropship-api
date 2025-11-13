from fastapi import FastAPI
from .routers import ingest, candidates, approve
from .database import Base, engine

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dropship Intelligence API",
    version="1.0.0"
)

app.include_router(ingest.router)
app.include_router(candidates.router)
app.include_router(approve.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Dropship API running"}
