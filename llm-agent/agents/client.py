from typing import Protocol, runtime_checkable
# Rimuovi l'import da ll_agent_pydantic che non serve più
from src.models import WeatherInfo, AgentResult

@runtime_checkable
class LLMClientProtocol(Protocol):
    async def generate(self, prompt: str) -> str:
        ...

class PydanticAIClienAdapter:
    def __init__(self, api_key: str):
        self._client = None 

    async def generate(self, prompt: str) -> str:
        return (
            '{"location": "Florence", "temperature_c": 26.5, "condition": "Sunny", '
            '"humidity_pct": 45, "forecast": ["Sunny", "Cloudy", "Rain"]}'
        )