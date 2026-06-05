#per usare ll-agent-pydantic come un pacchetto Python crea un file __init__.py vuoto nella cartella ll-agent-pydantic


# 🌤️ Type‑Safe LLM Agent with Pydantic AI

A tiny demo that shows how to:

* **Define a structured output** with Pydantic (`WeatherInfo`).
* **Call an LLM** (the example uses a mock client, replace with the real one).
* **Inject the LLM client** as a dependency, making the agent testable and provider‑agnostic.

## 📂 Repository layout

llm-agent-pydantic/ │ ├─ agent.py # WeatherAgent implementation ├─ models.py # Pydantic models (WeatherInfo, AgentResult) ├─ client.py # Dependency‑injection wrapper around the LLM client ├─ main.py # Demo script ├─ requirements.txt # dependencies └─ README.md

Copy

## 🚀 How to run

```bash
# 1️⃣ Clone the repo (or copy the files into a new folder)
git clone https://github.com/tuonome/llm-agent-pydantic.git
cd llm-agent-pydantic

# 2️⃣ (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the demo
python -m main
Note: The demo uses a mock LLM client that always returns the same JSON.
Replace PydanticAIClienAdapter with the real client you want to use (e.g., OpenAI, Anthropic, Gemini) and provide a valid API key.

🧩 What you learned
Concept	Where it appears
Structured output	models.py (WeatherInfo, AgentResult)
Function calling	client.generate() – the only place the LLM is invoked
Dependency injection	WeatherAgent.__init__(llm_client=…) – the agent receives any object that follows LLMClientProtocol
Type‑safety	Validation via WeatherInfo(**data_dict) – any mismatch raises ValidationError
