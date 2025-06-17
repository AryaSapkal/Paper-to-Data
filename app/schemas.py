from typing import Optional
from pydantic import BaseModel
from datetime import datetime



class Image(BaseModel):
    filename: str
    content: str
    time_created: datetime = datetime.now()
    rating: Optional[int] = None


