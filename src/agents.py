"""
AI Agents Module for Job Search Application.

This module defines all the AI agents (LLM chains) used for various tasks
including job search parsing, resume analysis, and feedback generation.
"""

import logging
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from prompts import *
from structure_outputs import *

# Configure logging
logger = logging.getLogger(__name__)


class Agents:
    """
    Collection of AI agents for job search and resume analysis.
    
    This class initializes and manages various LLM-based agents that perform
    different tasks in the workflow:
    - Job search input parsing
    - Job description summarization
    - Resume field extraction
    - Resume-job matching and feedback
    
    Attributes:
        job_input_agent: Agent for parsing user job search queries.
        job_summary_agent: Agent for extracting key info from job descriptions.
        resume_agent: Agent for extracting structured fields from resumes.
        resume_feedback_agent: Agent for generating feedback and similarity scores.
    """
    
    def __init__(self):
        """
        Initialize all AI agents with their respective models and prompts.
        
        Sets up:
        - Google Gemini LLM for text generation
        - HuggingFace embeddings for semantic search
        - Prompt templates for each agent
        - Structured output schemas
        """
        logger.info("Initializing AI agents")
        
        # Initialize LLM
        logger.debug("Loading Gemini 2.5 Flash Lite model")
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        
        # Initialize embeddings
        logger.debug("Loading HuggingFace embeddings model")
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        
        # Job Search Input Agent
        logger.debug("Setting up job searching agent")
        job_searching_prompt = PromptTemplate(
            template=JOB_SERCHING_PROMPT,
            input_variables=['user_prompt']
        )
        
        self.job_input_agent = (
            job_searching_prompt |
            llm.with_structured_output(JobInfo)
        )
        logger.debug("Job searching agent initialized")
        
        # Job Description Summary Agent
        logger.debug("Setting up job summary agent")
        job_description_template = PromptTemplate(
            template="""{job_description}""",
            input_variables=['job_description']
        )
        
        self.job_summary_agent = (
            job_description_template |
            llm.with_structured_output(Job_Summary)
        )
        logger.debug("Job summary agent initialized")
        
        # Resume Extraction Agent
        logger.debug("Setting up resume extraction agent")
        resume_template = PromptTemplate(
            template=RESUME,
            input_variables=['resume_text']
        )
        
        self.resume_agent = (
            resume_template | 
            llm.with_structured_output(Resume)
        )
        logger.debug("Resume extraction agent initialized")
        
        # Resume Feedback Agent
        logger.debug("Setting up resume feedback agent")
        resume_feedback_template = PromptTemplate(
            template=RESUME_FEADBACK,
            input_variables=['resume_skills', 'resume_profile', 'job_skills', 'job_info'],
            input_types={
                'resume_skills': List[str],
                'resume_profile': str,
                'job_skills': List[str],
                'job_info': str
            }
        )
        
        self.resume_feedback_agent = (
            resume_feedback_template |
            llm.with_structured_output(similar_and_feadback)
        )
        logger.debug("Resume feedback agent initialized")
        
        logger.info("All AI agents initialized successfully")
        
        