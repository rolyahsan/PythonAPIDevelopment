from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

hrrapi = FastAPI()


class Post(BaseModel):
    post_id: int
    job_title: str
    salary: float
    published: bool = False
    rating: Optional[int] = None


my_posts = [{"post_id": 1, "job_title": "Software QA Engineer", "salary": 125000, "published": False},
            {"post_id": 2, "job_title": "QA Analyst", "salary": 98000, "rating": 4},
            {"post_id": 3, "job_title": "Manual Tester", "salary": 75000, "published": True, "rating": 5}]