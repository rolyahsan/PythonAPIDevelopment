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


def find_post(post_id):
    for p in my_posts:
        if p['post_id'] == post_id:
            return p


@hrrapi.get("/")
def root():
    return {"Welcome": "to hrrAPI"}


@hrrapi.get("/posts")
def get_post():
    return {"message": my_posts}


@hrrapi.get("/posts/{post_id}")
def get_post(post_id):
    post = find_post(int(post_id))
    return {"message": post}


@hrrapi.post("/posts")
def create_post(post: Post):
    print(post)
    return {"new_post": post}
