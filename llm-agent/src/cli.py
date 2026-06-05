import asyncio
from agents.client import PydanticAIClienAdapter
from agents.agent import WeatherAgent # NOTA: è agent, non client!

async def main():
    # Se non hai l'API key, usa direttamente il mock
    api_key = "demo-key"
    llm_client = PydanticAIClienAdapter(api_key=api_key)
    agent = WeatherAgent(llm_client=llm_client)
    
    result = await agent.get_forecast("Rome")
    
    print("\n=== Agent Result ===")
    # Se usi Pydantic v2, .json() è diventato .model_dump_json()
    # Prova questo se .json() ti dà errore
    print(result.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())