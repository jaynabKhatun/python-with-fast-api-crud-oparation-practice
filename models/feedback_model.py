from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class FeedbackBase(BaseModel):
    comment: Optional[str] = None
    rating: int = Field(..., ge=1, le=5,
                        description="Rating must be between 1 and 5")
    userId: str
    mealId: str
    feedbackTime: datetime


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackResponse(FeedbackBase):
    _id: str
