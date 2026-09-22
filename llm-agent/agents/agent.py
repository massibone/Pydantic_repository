# agent.py
import json
from typing import Any

from pydantic import ValidationError
from src.models import WeatherInfo, AgentResult
from agents.client import LLMClientProtocol


class WeatherAgent:
    """
    A simple agent that asks an LLM for a weather forecast and returns a
    strongly‑typed `AgentResult`.
    """

    def __init__(self, llm_client: LLMClientProtocol):
        self._llm = llm_client

    async def get_forecast(self, location: str) -> AgentResult:
        """
        Calls the LLM, parses the JSON response, and returns a validated
        `AgentResult`.  All errors are caught and turned into a friendly
        `AgentResult` with `success=False`.
        """
        prompt = f"Give me the current weather and 3‑day forecast for {location}. " \
                 "Return ONLY a JSON object that matches the WeatherInfo schema."

        try:
            raw_json = await self._llm.generate(prompt)
            # Parse the JSON string
            data_dict = json.loads(raw_json)

            # Validate / convert to the Pydantic model – this is the **type‑safe** part
            weather = WeatherInfo(**data_dict)

            return AgentResult(success=True, data=weather)

        except (json.JSONDecodeError, ValidationError) as exc:
            # Any problem (bad JSON, missing fields, wrong types) ends up here
            return AgentResult(success=False, error=str(exc))
            
