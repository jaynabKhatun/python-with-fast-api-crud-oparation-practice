
from pydantic import BaseModel
from typing import Optional

# User Schema


class User(BaseModel):
    name: str
    address: str
    phone: str
    role: str
    department: str
    category: Optional[str] = None  # Optional Field
