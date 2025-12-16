from agents import Agents
from state import GraphState,JobInfo,Job
from tools.scraping_tools import *

class Nodes:
    def __init__(self):
        self.agents = Agents()
        
    def job_searching_node(self,state : GraphState) -> GraphState:
        user_input = state['user_input']
        res = self.agents.job_input_agent.invoke({'user_prompt':user_input})
        job_info_dict =res.model_dump(
                    mode="json",
                    exclude=['days','jobType','experience_level'],
                    exclude_none=True
                    )
        scrap_job = linkedin_scrapper(job_info_dict)
        l = []
        for item in scrap_job.iterate_items():
            l.append(Job(**item))
        return {'jobs':l}
    
    
        
        