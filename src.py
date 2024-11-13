from llama_index.tools.finance import FinanceAgentToolSpec

import os


POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY')
FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')




tool_spec = FinanceAgentToolSpec(
        POLYGON_API_KEY,
        FINNHUB_API_KEY,
        NEWS_API_KEY,
        ALPHA_VANTAGE_API_KEY
    )



