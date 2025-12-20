from pydantic import BaseModel
from typing import List,TypedDict,Set,Annotated
import operator

class Job(BaseModel):
    id : str
    url : str
    title : str
    location: str
    companyName: str 
    companyUrl:str
    recruiterName:str
    recruiterUrl:str
    experienceLevel: str
    contractType:str
    workType:str
    sector: str
    salary:  str
    applyType: str
    applyUrl:str 
    postedTimeAgo:str  
    postedDate: str
    applicationsCount: str
    description: str

class Job_Info_state(BaseModel):
    title : str  | None
    location : str | None
    datePosted : str | None
    companyName : List[str] | None
    companyId : List[str] | None
    skipJobId : List[str] | None
    remote : List[str] | None
    experienceLevel : List[str] | None
    contractType : List[str] | None
    limit : int | None

class Job_Output(TypedDict):
      job_info = str
      job_skills = List[str]
      similarity = int
      id = int
      feedback = int

class Resume_Fields(BaseModel):
    skills : List[str]
    Profile : str
    Projects : List[str]
    Certifications : List[str]
    Experience : List[str]   
    Education : List[str]

class GraphState(TypedDict):
    user_input : str
    job_info : Job_Info_state
    resume_text : str
    jobs : List[Job]
    visited_ids = Set[int]
    job_outputs = Annotated[List[Job_Output], operator.add]
    resume_fields = Resume_Fields
    


{
  "title": "Java",
  "location": "New York",
  "datePosted": "r604800",
  "companyName": [
    "Google",
    "Apple"
  ],
  "companyId": [
    "1441",
    "162479"
  ],
  "contractType": [
    "F",
    "P"
  ],
  "experienceLevel": [
    "1",
    "2"
  ],
  "remote": [
    "2",
    "3"
  ],
  "limit": 100,
  "urlParam": [
    {
      "key": "f_TPR",
      "value": "r3600"
    }
  ],
  "skipJobId": [
    "4219847745",
    "4219847746"
  ]
}

{'id': '4327194257', 
 'url': 'https://in.linkedin.com/jobs/view/data-scientist-i-at-swiggy-4327194257',
 'title': 'Data Scientist I',
 'location': 'Bengaluru, Karnataka, India',
 'companyName': 'Swiggy', 
 'companyUrl': 'https://in.linkedin.com/company/swiggy-in', 
 'recruiterName': '',
 'recruiterUrl': '',
 'experienceLevel': 'Entry level', 
 'contractType': 'Full-time',
 'workType': 'Engineering and Information Technology', 
 'sector': 'Technology, Information and Internet', 
 'salary': '', 
 'applyType': 'EASY_APPLY', 
 'applyUrl': 'https://in.linkedin.com/jobs/view/data-scientist-i-at-swiggy-4327194257', 
 'postedTimeAgo': '19 hours ago', 
 'postedDate': '2025-12-12T00:00:00.000Z',
 'applicationsCount': 'Over 200 applicants', 
 'description': """Job Profile: Data ScientistLocation : Bangalore | KarnatakaYears of Experience : 0 - 3About The Team & RoleData Science and applied ML is ingrained deeply in decision making and product development at Swiggy. Our data scientists work closely with cross-functional teams to ship end-to-end data products, from formulating the business problem in mathematical/ML terms to iterating on ML/DL methods to taking them to production. We own or co-own several initiatives with
 a direct line of sight to impact on customer experience as well as business metrics. We also encourage open sharing of ideas and publishing in internal and external avenuesWhat will you get to do here?You will leverage your strong ML/DL/Statistics background to build new and next generation of ML based solutions to improve the quality of ads recommendation and leverage various optimization techniques to improve the campaign performance.You will mine and extract relevant information 
 from Swiggy's massive historical data to help ideate and identify solutions to business and CX problems.You will work closely with engineers/PMs/analysts on detailed requirements, 
 technical designs, and implementation of end-to-end inference solutions at Swiggy scale.You will stay abreast with the latest in ML research for Ads Bidding algorithms, 
 Recommendation Systems related areas and help adapt it to Swiggy's problem statements.
 You will publish and talk about your work in internal and external forums to both technical and layman audiences.Opportunity to work on challenging and impactful projects in the logistics domainCollaborate with cross-functional teams, 
 including software developers and product managers, to integrate data-driven solutions into our systemsDevelop and deploy machine learning and deep learning modelsTake ownership of projects from inception to delivery, ensuring high-quality 
 and impactful results.What qualities are we looking for?Bachelors or Masters degree in a quantitative field with 0-3 years of industry/research lab experienceRequired: Excellent problem solving skills, ability to deconstruct and formulate solutions 
 from first-principlesRequired: Depth and hands-on experience in applying ML/DL, statistical techniques to business problemsPreferred: Experience working with ‘big data’ and shipping ML/DL models to productionRequired: Strong proficiency in Python, SQL, 
 Spark, TensorflowRequired: Strong spoken and written communication skillsBig plus: Experience in the space of ecommerce and logisticsExperience in Generative AIProven track record of developing and shipping ML and DL data productsExperience in Agentic AI , 
 LLMS and NLPProficiency in PythonVisit our tech blogs to learn more about some the challenges we deal with:https://bytes.swiggy.com/the-swiggy-delivery-challenge-part-one-6a2abb4f82f6https://bytes.swiggy.com/how-ai-at-swiggy-is-transforming-convenience-eae0a32055aehttps://bytes.swiggy.com/decoding-food-intelligence-at-swiggy-5011e21dbc86We 
 are an equal opportunity employer and all qualified applicants will receive consideration for employment without regard to race, colour, religion, sex, disability status, or any other characteristic protected by the law.", 'descriptionHtml': 'Job Profile: Data Scientist<br><br>Location : 
 Bangalore | Karnataka<br><br>Years of Experience : 0 - 3<br><br><strong>About The Team &amp; Role<br><br></strong>Data Science and applied ML is ingrained deeply in decision making and product development at Swiggy. Our data scientists work closely with cross-functional teams to ship 
 end-to-end data products, from formulating the business problem in mathematical/ML terms to iterating on ML/DL methods to taking them to production. 
 We own or co-own several initiatives with a direct line of sight to impact on customer experience as well as business metrics. We also encourage open sharing of ideas and publishing in internal and external avenues<br><br><strong>What will you get to do here?<br><br></strong><ul><li>
 You will leverage your strong ML/DL/Statistics background to build new and next generation of ML based solutions to improve the quality of ads recommendation 
 and leverage various optimization techniques to improve the campaign performance.</li><li>\
 You will mine and extract relevant information from Swiggy&apos;s massive historical data to help ideate and identify solutions to business and CX problems.</li><li>
 You will work closely with engineers/PMs/analysts on detailed requirements, technical designs, and implementation of end-to-end inference solutions at Swiggy scale.</li><li>You will stay abreast with the latest in ML research for Ads Bidding algorithms, Recommendation Systems related areas 
 and help adapt it to Swiggy&apos;s problem statements.</li><li>You will publish and talk about your work in internal and external forums to both technical and layman audiences.</li><li>Opportunity to work on challenging and impactful projects in the logistics domain</li><li>Collaborate with 
 cross-functional teams, including software developers and product managers, to integrate data-driven solutions into our systems</li><li>Develop and deploy machine learning and deep learning models</li><li>Take ownership of projects from inception to delivery, ensuring high-quality and impactful 
 results.<br><br></li></ul><strong>What qualities are we looking for?<br><br></strong><ul><li>Bachelors or Masters degree in a quantitative field with 0-3 years of industry/research lab experience</li><li>Required: Excellent problem solving skills, ability to deconstruct and formulate solutions from 
 first-principles</li><li>Required: Depth and hands-on experience in applying ML/DL, statistical techniques to business problems</li><li>Preferred: Experience working with &#x2018;big data&#x2019; and shipping ML/DL models to production</li><li>Required: Strong proficiency in Python, SQL, Spark, Tensorflow</li><li>
 Required: Strong spoken and written communication skills</li><li>Big plus: Experience in the space of ecommerce and logistics</li><li>Experience in Generative AI</li><li>Proven track record of developing and shipping ML and DL data products</li><li>Experience in Agentic AI , LLMS and NLP</li><li>Proficiency in Python<br>
 <br></li></ul><strong>Visit our tech blogs to learn more about some the challenges we deal with:<br><br></strong>https://bytes.swiggy.com/the-swiggy-delivery-challenge-part-one-6a2abb4f82f6<br><br>https://bytes.swiggy.com/how-ai-at-swiggy-is-transforming-convenience-eae0a32055ae<br><br>https://bytes.swiggy.com/decoding-food-intelligence-at-swiggy-5011e21dbc86<br>
 <br>We are an equal opportunity employer and all qualified applicants will receive consideration for employment without regard to race, colour, religion, sex, disability status, or any other characteristic protected by the law."""}