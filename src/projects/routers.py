from fastapi import APIRouter, status, Response, Depends, HTTPException
from .models import Project
from .repositories import ProjectRepository
from .schemas import ProjectRequest, ProjectResponse
from core.database import get_db, engine, Base
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/projects", response_model=list[ProjectResponse], status_code=status.HTTP_200_OK, name="get_all_projects", tags=["projects"])
def get_all(db: Session = Depends(get_db)):
    projects = ProjectRepository.get_all(db)
    return [ProjectResponse(**project.__dict__) for project in projects]

@router.get("/projects/{id}", response_model=ProjectResponse, status_code=status.HTTP_200_OK, name="get_project_by_id", tags=["projects"])
def get_by_id(id: int, db: Session = Depends(get_db)):
    project = ProjectRepository.get_by_id(db, id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Projeto não encontrado.")
    return ProjectResponse(**project.__dict__)

@router.post("/projects", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED, name="create_project", tags=["projects"])
def create(project_request: ProjectRequest, db: Session = Depends(get_db)):
    project = Project(**project_request.__dict__)
    project = ProjectRepository.save(db, project)
    return ProjectResponse(**project.__dict__)