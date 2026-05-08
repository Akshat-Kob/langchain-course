from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
# from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches the internet
    Args:
        query: The search query.
    Returns:
        A string containing the search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

# llm = ChatGroq(model="llama-3.1-8b-instant")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
