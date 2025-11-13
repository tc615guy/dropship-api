from pydantic import BaseModel


class IngestRequest(BaseModel):
    domain: str


class ApproveRequest(BaseModel):
    id: int


class ProductResponse(BaseModel):
    id: int
    url: str
    name: str
    reviews: int
    rating: float
    price: float

    class Config:
        orm_mode = True
