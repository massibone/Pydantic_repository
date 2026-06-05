from pydantic import BaseModel
from typing import List, Optional

class WeatherInfo(BaseModel):
    location: str
    temperature_c: float
    condition: str
    humidity_pct: int
    forecast: List[str]

class AgentResult(BaseModel):
    success: bool
    data: Optional[WeatherInfo] = None
    error: Optional[str] = None