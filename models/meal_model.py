from pydantic import BaseModel
from typing import List


class MealModel(BaseModel):
    
    name: str
    rawItem: List[str]
    price: int
