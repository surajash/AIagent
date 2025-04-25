from pydantic import BaseModel
from typing import List

class AlertRequest(BaseModel):
    metrics: List[float]
