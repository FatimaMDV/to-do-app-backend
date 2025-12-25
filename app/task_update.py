from typing import Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field

class UPDATE(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    starts: Optional[datetime] = None
    due_date: Optional[datetime] = None
    is_done: Optional[bool] = None
    level: Optional[Literal["easy", "medium", "hard"]] = None
    priority: Optional[Literal["low", "normal", "high"]] = None