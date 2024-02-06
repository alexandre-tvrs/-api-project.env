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
        from_attributes = True