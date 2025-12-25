from typing import Optional, Literal
from datetime import datetime
from pydantic import BaseModel

class READ(BaseModel):
    id: int
    title: str 
    description: Optional[str] 
    starts: Optional[datetime] 
    due_date: Optional[datetime] 
    done: bool 
    level: Literal["easy", "medium", "hard"]
    priority: Literal["low","normal","high"]
    created_at: datetime
    updated_at: Optional[datetime] = None