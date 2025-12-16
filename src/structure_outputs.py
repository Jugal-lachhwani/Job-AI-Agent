from pydantic import BaseModel,Field,computed_field
from typing import List
from enum import Enum

class JobType(str,Enum):
    REMOTE = 'remote'
    HYBRID = 'hybrid'
    ONSITE = 'onsite'

class ExperienceLevel(str, Enum):
    Internship = "Internship"
    Entry_level = "Entry_level"
    Associate = "Associate"
    Mid_Senior_level = "Mid_Senior_level"
    Director = "Director"
    Executive = "Executive"

class JobInfo(BaseModel):
    title : str | None = Field(default=None,description= "Primary job title or role to search for.This represents the main occupation or position of interest." ,examples=['AI engineer','Data Scientist','SQL','Java','Software Engineer'])
    location : str | None = Field(default=None,description= "The name of the country where job needs to be find, If any city name is entered then think of the contry in which the city exist",examples=['India','America'])
    days : int | None = Field(default=7,description= "Job posted within the last days ",examples=[1,3,7,14])
    companyName : List[str] | None = Field(default=None,description= "The List of companies which needs to consider first or which is only needs to considered, ordered by priority ",examples=['Google','Microsoft'])
    companyId : List[str] | None = Field(default=None,description= "The List of Ids of the companies which needs to consider first or which is only needs to considered, ordered by priority ",examples=['21345','5567483'])
    skipJobId : List[str] | None = Field(default=None,description= "The List of Ids of the companies which needs to  be skiped or not considered",examples=['21345','5567483'])
    jobType : List[JobType] | None = Field(default=None,description= "This is the list of type of job the user preferred, ordered by priority ",examples=[['remote','hybrid'],['onsite']])
    experience_level : List[ExperienceLevel] | None = Field(default=None,description= "Preferred experience levels for the job, ordered by priority (from most to least preferred).")
    # typeOfContract : List[str] | None = Field(default=None,description= "The type of the ontract preffered by the user rankwise ",examples=[['Part_time','Full_time']])
    limit : int | None = Field(default=3,description= "The number of jobs the user wants to find even if the user will say a big number limit it up to 3",le=3,ge=1,examples=[3,1,2])
    
    @computed_field
    @property
    def datePosted(self) -> str:
        return "r" + str(self.days * 86400)

    @computed_field
    @property
    def remote(self) -> List[int] | None:
        if not self.jobType:
            return None

        mapping = {
            JobType.ONSITE: '1',
            JobType.REMOTE: '2',
            JobType.HYBRID: '3',
        }

        return [mapping[jt] for jt in self.jobType]
    
    @computed_field
    @property
    def experienceLevel(self) -> List[str] | None:
        if not self.experience_level:
            return None

        mapping = {
            ExperienceLevel.Internship: "1",
            ExperienceLevel.Entry_level: "2",
            ExperienceLevel.Associate: "3",
            ExperienceLevel.Mid_Senior_level: "4",
            ExperienceLevel.Director: "5",
            ExperienceLevel.Executive: "6",
        }

        return [mapping[ctype] for ctype in self.experience_level]  
    
    