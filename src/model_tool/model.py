from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

tavily = TavilySearch()
llm = ChatGroq(model="deepseek-r1-distill-llama-70b")


