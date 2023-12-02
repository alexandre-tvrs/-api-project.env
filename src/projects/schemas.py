from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    icon: str


class ProjectRequest(Project):
    ...


class ProjectResponse(Project):
    id: int

    class Config:
        orm_mode = True