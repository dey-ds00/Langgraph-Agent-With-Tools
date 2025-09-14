from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import tools_condition,ToolNode
from model_tool.tools import llm_with_tools,tools
from initiate_state import State


def call_tool(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

graph_builder = StateGraph(State)

graph_builder.add_node("call_tool",call_tool)
graph_builder.add_node("tools",ToolNode(tools))

graph_builder.add_edge(START,"call_tool")
graph_builder.add_conditional_edges("call_tool",tools_condition)
graph_builder.add_edge("call_tool",END)

graph = graph_builder.compile()
