from typing import Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field

class DELETE(BaseModel):
    deleted: bool
    id: int