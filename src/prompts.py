"""
Prompt Templates for AI Agents.

This module contains all the prompt templates used by various AI agents
in the job search and resume analysis workflow.
"""

# Job Search Prompt Template
JOB_SERCHING_PROMPT = """
        You are job searching helping agent you need to pass the 
        data to job searchng API for that you need to structure the 
        output from the given user prompt : {user_prompt}
        """


# Resume Analysis Prompt Template
RESUME = """
        You are thoughtful agent help in extracting the Important features 
        from the resume text. Resume text is not structures as it is extracted 
        from a knowledge so use your llm skills to extract the following:
        Skills : The main programing and technikal skills focus more on the domain specific skills rather than soft skills
        Profile : The brief info about the user found in the resume text
        Projects : The Projects that are built by the user found in the resume
        Certifications : THe certifications of the user in the resume
        Experience : The Experience of the user mentioned in the resume
        Education : The education oof the yser found in the resume
        The Remuse text is : {resume_text}
"""


# Resume Feedback and Similarity Prompt Template
RESUME_FEEDBACK = """
        You are a agent that hepls users to find the best job be hepling them improve there resume
        Your job is to tell what are the things that lack In there resume.
        What are those keywords, skills or projects what will help him to improve the resume,
        Along with that give the similarity score between 0 to 100 how well the jon suits the user
        
        Resemu text : {resume_text}
        Job description : {job_description}
"""