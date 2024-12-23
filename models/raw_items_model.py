from pydantic import BaseModel


class RawItemModel(BaseModel):

    title: str
    details: str
    price: int
    quantity: int
    addedBy: int
