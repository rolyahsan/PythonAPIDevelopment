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

