from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from prompts import *
from structure_outputs import *


class Agents:
    def __init__(self):
        llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
            )
        
        job_searching_prompt = PromptTemplate(
            template = JOB_SERCHING_PROMPT,
            input_variables=['user_prompt']
            )
        
        self.job_input_agent = (
            job_searching_prompt |
            llm.with_structured_output(JobInfo)
        )
        
        job_description_template = PromptTemplate(template="""{job_description}""",input_variables=['job_description'])
        
        self.job_summary_agent = (
            job_description_template |
            llm.with_structured_output(Job_Summary)
        )
        
        resume_template = PromptTemplate(template=RESUME,
        input_variables=['resume_text'])
        
        self.resume_agent = (
            resume_template | 
            llm.with_structured_output(Resume)
        )
        
        resume_feedback_template = PromptTemplate(template = RESUME_FEADBACK,
                                          input_variables=['resume_skills','resume_profile','job_skills','job_info'],
                                          input_types={'resume_skills':List[str],'resume_profile':str,'job_skills':List[str],'job_info':str})
        
        self.resume_feedback_agent = (
        resume_feedback_template |
        llm.with_structured_output(similar_and_feadback)
        )
        
        