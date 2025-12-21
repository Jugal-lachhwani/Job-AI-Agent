from langgraph.graph import END, StateGraph, START
from src.state import GraphState
from src.nodes import Nodes

class Workflow():
    def __init__(self):
        workflow = StateGraph(GraphState)
        nodes = Nodes()
        
        # Add all nodes
        workflow.add_node("job_searching_node", nodes.job_searching_node)
        workflow.add_node("resume_text_extractor", nodes.resume_text_extractor)
        workflow.add_node("extract_fields_from_resume", nodes.extract_fields_from_resume)
        workflow.add_node("extract_fields_from_job_desc", nodes.extract_fields_from_job_desc)
        workflow.add_node("Feadback_and_similarity", nodes.Feadback_and_similarity)
        
        # Branch 1: Job Description Path
        workflow.add_edge(START, "job_searching_node")
        workflow.add_edge("job_searching_node", "extract_fields_from_job_desc")
        
        # Branch 2: Resume Path
        workflow.add_edge(START, "resume_text_extractor")
        workflow.add_edge("resume_text_extractor", "extract_fields_from_resume")
        
        # Both branches converge to Feedback node (LangGraph waits for both)
        workflow.add_edge("extract_fields_from_job_desc", "Feadback_and_similarity")
        workflow.add_edge("extract_fields_from_resume", "Feadback_and_similarity")
        
        # End workflow
        workflow.add_edge("Feadback_and_similarity", END)
        
        self.app = workflow.compile()
        
        
        