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
        
        