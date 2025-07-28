import os
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent, AgentType

# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2", temperature=0.7)

# Initialize the Wikipedia API wrapper
wikipedia_api_wrapper = WikipediaAPIWrapper()

# Create the Wikipedia tool
wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)

# List of tools available to the agent
tools = [wikipedia_tool]

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # A common agent type for tool usage
    verbose=True,  # Set to True to see the agent's thought process
    handle_parsing_errors=True # Handle potential parsing errors during execution
)

# Invoke the agent with a query
query = "Tell me about the history of the internet."
agent.run(query)