from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class CREATE(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None
    starts: Optional[datetime] = None
    due_date: Optional[datetime] = None
    done: bool = False
    
    