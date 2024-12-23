from pydantic import BaseModel
from typing import List


class MealModel(BaseModel):
    id: int
    name: str
    rawItem: List[str]
    price: int
