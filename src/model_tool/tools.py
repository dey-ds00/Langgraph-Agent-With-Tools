from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from model_tool.model import llm,tavily

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1))
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

tools = [wiki,arxiv,tavily]
llm_with_tools=llm.bind_tools(tools)