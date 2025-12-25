from typing import Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field

class CREATE(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None
    starts: Optional[datetime] = None
    due_date: Optional[datetime] = None
    is_done: bool = False
    level: Literal["easy", "medium", "hard"] = "easy"
    priority: Literal["low","normal","high"] = "normal"
    
    