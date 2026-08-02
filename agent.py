from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
from langchain.agents import create_agent
from rag import setup_vector_store, query_vector_store

# Initialize Chroma collection
vector_collection = setup_vector_store()


@tool
def search_document(query: str) -> str:
    """Search the user's document for relevant information."""
    return query_vector_store(vector_collection, query)


def get_rag_agent():
    """Initializes and returns the LangChain agent."""
    tools = [search_document]
    llm = ChatAnthropic(model="claude-haiku-4-5")
    agent = create_agent(llm, tools)
    return agent
