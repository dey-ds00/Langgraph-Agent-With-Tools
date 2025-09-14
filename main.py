from workflow.graphflow import graph

def main():
    rslt = graph.invoke({"messages":"What is the current prize of MSI GAMING Laptop"})
    print(rslt["messages"][-1].content)

if __name__=="__main__":
    main()