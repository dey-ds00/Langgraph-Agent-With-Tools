# LangGraph Agent with Tools

## This project demonstrates how to build an agentic workflow using LangGraph LangChain community tools and an LLM bound with external APIs.

### The agent can:

  **Query Wikipedia for factual information.**

  **Query Arxiv for research papers.**

  **Use custom tools (e.g., Tavily).**

  **Process user queries through a graph-based workflow.**

# 🚀 Features

  ## Wikipedia Search via WikipediaQueryRun.

  ## Arxiv Search via ArxivQueryRun.

  ## Custom Tool Support (e.g., Tavily).

  ## LangGraph-based Workflow with tool nodes and conditional branching.

  ## Visualization of the graph using IPython's Mermaid png.


⚙️ Installation

  1. Clone the repository<br>
     *git clone https://github.com/your-username/langgraph-agent-with-tools.git*<br>
     *cd langgraph-agent-with-tools*<br>


  2. Create a virtual environment (recommended)<br>
     *uv venv*<br>
     *source venv/bin/activate*   # On Linux/Mac<br>
     *venv\Scripts\activate*      # On Windows<br>
     
  3. Install dependencies<br>
     *uv pip install -r requirements.txt*<br>
     or *uv sync*<br>
     
🔮 Future Improvements:
      Add more domain-specific tools (e.g., weather, finance, news).
      Integrate memory into the workflow.
      Extend graph visualization for debugging agent workflows.



