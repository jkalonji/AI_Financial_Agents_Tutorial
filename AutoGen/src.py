import autogen
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import datetime
import os

OPENAI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
# Configuration du modèle LLM
llm_config = {
    "config_list": [{"model": "gpt-4", "api_key": OPENAI_API_KEY}],
    "temperature": 0
}

# Création de l'agent assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message=f"""You are a helpful AI assistant that can write Python code to create plots and analyze stock data. 
    If you encounter abug, think critically and step by step to resolve it, and re-submit your code.
    Use polars instead of pandas. Adapt the column names so that they can be easily accessed"""
)

# Création de l'agent assistant pour la révision du code
code_reviewer = AssistantAgent(
    name="code_reviewer",
    llm_config=llm_config,
    system_message="""You are an expert Python code reviewer. Your task is to review the code written by the assistant, 
    identify any issues or potential improvements, and suggest corrections. Focus on:
    1. Correctness of the code
    2. Efficiency and performance
    3. Best practices and coding standards
    4. Potential bugs or edge cases
    Provide your feedback in a clear and constructive manner."""
)

# Création de l'agent générateur de graphiques
graph_generator = AssistantAgent(
    name="graph_generator",
    llm_config=llm_config,
    system_message="""You are a specialized AI assistant focused on generating graphs and visualizations. Your tasks include:
    1. Creating two different graphs for a dashboard using Python and libraries like Matplotlib or Plotly.
    2. Ensuring the graphs are visually appealing and informative.
    3. Saving the graphs as image files.
    4. Providing code to display these graphs in a simple dashboard layout.
    Use polars for data manipulation if needed. Make sure to use dark mode for better visibility."""
)

# Création de l'agent proxy utilisateur
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    }
)

# Message initial
today = datetime.datetime.now().date()
message = f"""Today is {today}. Create a dashboard with two graphs:
1. A correlation matrix between price movements for BTC and ETH.
2. A line chart showing the price trends of BTC and ETH over the last month.
Make sure the code is in markdown code blocks and save the figures to files.
Use dark mode to display the data. Create a simple dashboard layout to display both graphs.
Open the dashboard at the end of your code execution."""

# Initiation du chat
#user_proxy.initiate_chat(
#    assistant,
#    message=message
#)


# Création d'un GroupChat
groupchat = GroupChat(
    agents=[user_proxy, assistant, code_reviewer, graph_generator],
    messages=[],
    max_round=7
)

# Création d'un manager pour le GroupChat
manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)


# Initiation de la conversation
user_proxy.initiate_chat(
    manager,
    message=message
)
