from agents import Agents
from state import *
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

    def resume_text_extractor(self,state:GraphState) -> GraphState:
        from pypdf import PdfReader

        reader = PdfReader("E:\Genai_Projects\\Job_search_Agent\\Resume.pdf")
        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        return {'resume_text': text}   
        
    
    def extract_fields_from_resume(self,state:GraphState) -> GraphState:
        resume_text = state['resume_text']
        res = self.agents.resume_agent.invoke({'resume_text':resume_text})
        return {'resume_fields':res}
    
    def extract_fields_from_job_desc(self,state : GraphState) -> GraphState:
        visited_set = state['visited_ids']
        job_summary_model_list = []
        for job in state['jobs']:
            if job.id not in visited_set:
                visited_set.add(job.id)
                job_summary = self.agents.job_summary_agent.invoke({'job_description':job.description})
                job_summary_model = Job_Summary(
                    job_info=job_summary.job_info,
                    job_skills=job_summary.job_skills,
                    id=job.id
                )
                job_summary_model_list.append(job_summary_model)
                
        return {'job_summaries':job_summary_model_list,'visited_ids':visited_set}

    def Feadback_and_similarity(self,state : GraphState) -> GraphState:
        visited_set = state['visited_ids_feadback']
        job_feedback_model_list = []
        for job in state['jobs_summaries']:
            if job.id not in visited_set:
                visited_set.add(job.id)
                resume_skills = state['resume_fields'].skills
                resume_profile = state['resume_fields'].profile
                job_skills = job.job_skills
                job_info = job.job_info
                
                job_feedback = self.agents.resume_feedback_agent.invoke({
                    'resume_skills':resume_skills,
                    'resume_profile':resume_profile,
                    'job_skills':job_skills,
                    'job_info':job_info})
                
                job_feedback_model = Job_Feadback(
                    job_info=job_feedback.similarity,
                    skills=job_feedback.feedback,
                    job_id=job.id
                )
                job_feedback_model_list.append(job_feedback_model)
                
        return {'job_feedbacks':job_feedback_model_list,'visited_ids_feedback':visited_set}
    
    

    
        
        