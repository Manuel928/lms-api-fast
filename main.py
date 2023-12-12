from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from api import users, sections, courses

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Emmanuel",
        "email": "emma@test.com"
    },
    license_info={
        "name": "Apache 2.0"
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)