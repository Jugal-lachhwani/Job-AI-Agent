from pydantic import BaseModel,Field,computed_field
from typing import List
from enum import Enum

class JobType(str,Enum):
    REMOTE = 'remote'
    HYBRID = 'hybrid'
    ONSITE = 'onsite'

class ContractType(str, Enum):
    FULL_TIME = "Full_time"
    PART_TIME = "Part_time"
    CONTRACT = "Contract"
    TEMPORARY = "Temporary"
    INTERNSHIP = "Internship"
    APPRENTICESHIP = "Apprenticeship"
"""F	Full-time
P	Part-time
C	Contract
T	Temporary
I	Internship
A	Apprenticeship"""
    
class JobInfo(BaseModel):
    title : str | None = Field(default=None,description= "Primary job title or role to search for.This represents the main occupation or position of interest." ,examples=['AI engineer','Data Scientist','SQL','Java','Software Engineer'])
    location : str | None = Field(default=None,description= "The place where the job needs to be find",examples=['India','Banglore','America','Los Angeles','Rajasthan'])
    days : int | None = Field(default=7,description= "Job posted within the last days ",examples=[1,3,7,14])
    company_name : List[str] | None = Field(default=None,description= "The List of companies which needs to consider first or which is only needs to considered",examples=['Google','Microsoft'])
    companyId : List[str] | None = Field(default=None,description= "The List of Ids of the companies which needs to consider first or which is only needs to considered",examples=['21345','5567483'])
    skipJobId : List[str] | None = Field(default=None,description= "The List of Ids of the companies which needs to  be skiped or not considered",examples=['21345','5567483'])
    jobType : List[JobType] | None = Field(default=None,description= "This is the list of type of job the user preferred rankwise",examples=[['remote','hybrid'],['onsite']])
    experienceLevel : List[str] | None = Field(default=None,description= "This is the experience level needed for the job preferred by the user in years rankwise",examples=['1','2','3'])
    typeOfContract : List[ContractType] | None = Field(default=None,description= "The type of the ontract preffered by the user rankwise ",examples=[['Part_time','Full_time']])
    limit : int | None = Field(default=3,description= "The number of jobs the user wants to find even if the user will say a big number limit it up to 3",le=3,ge=1,examples=[3,1,2])
    
    @computed_field
    @property
    def date_posted(self) -> str:
        return "r" + str(self.days * 86400)

    @computed_field
    @property
    def job_type_codes(self) -> List[int] | None:
        if not self.jobType:
            return None

        mapping = {
            JobType.ONSITE: 1,
            JobType.REMOTE: 2,
            JobType.HYBRID: 3,
        }

        return [mapping[jt] for jt in self.jobType]
    
    @computed_field
    @property
    def contract_codes(self) -> List[str] | None:
        if not self.typeOfContract:
            return None

        mapping = {
            ContractType.FULL_TIME: "F",
            ContractType.PART_TIME: "P",
            ContractType.CONTRACT: "C",
            ContractType.TEMPORARY: "T",
            ContractType.INTERNSHIP: "I",
            ContractType.APPRENTICESHIP: "A",
        }

        return [mapping[ctype] for ctype in self.typeOfContract]  
            