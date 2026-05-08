from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
# from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """ Schema for a source used by the agent """
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """ Schema for the agent response with answer and sources"""
    answer: str = Field(description="The Agent's answer to the user's query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used by the agent to generate the answer")

# llm = ChatGroq(model="llama-3.1-8b-instant")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
