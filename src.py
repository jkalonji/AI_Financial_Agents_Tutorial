from llama_index.tools.finance import FinanceAgentToolSpec
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
import os

POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY')
FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
GPT_MODEL_NAME = "gpt-4o-mini"

tool_spec = FinanceAgentToolSpec(
        POLYGON_API_KEY,
        FINNHUB_API_KEY,
        NEWS_API_KEY,
        ALPHA_VANTAGE_API_KEY
    )
def create_agent(
    polygon_api_key: str,
    finnhub_api_key: str,
    alpha_vantage_api_key: str,
    newsapi_api_key: str,
    openai_api_key: str,
) -> OpenAIAgent:
    tool_spec = FinanceAgentToolSpec(
        polygon_api_key,
        finnhub_api_key,
        alpha_vantage_api_key,
        newsapi_api_key,
    )
    llm = OpenAI(temperature=0, model=GPT_MODEL_NAME, api_key=openai_api_key)
    return OpenAIAgent.from_tools(
        tool_spec.to_tool_list(), llm=llm, verbose=True
    )
agent = create_agent(
    POLYGON_API_KEY,
    FINNHUB_API_KEY,
    ALPHA_VANTAGE_API_KEY,
    NEWS_API_KEY,
    OPENAI_API_KEY,
)

response = agent.chat("Provide a trading strategy to invest in the automotive sector")
print(response)

# Écrire la réponse dans un fichier markdown
with open("financial-guidelines.md", "w") as file:
    file.write("# Financial Guidelines\n\n")
    file.write(str(response))