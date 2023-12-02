from sqlalchemy.orm import Session
from .models import Project


class ProjectRepository:
    @staticmethod
    def get_all(db: Session) -> list[Project]:
        return db.query(Project).all()
    
    @staticmethod
    def get_by_id(db: Session, id: int) -> Project:
        return db.query(Project).filter(Project.id == id).first()
    
    @staticmethod
    def get_by_name(db: Session, name: str) -> Project:
        return db.query(Project).filter(Project.name == name).first()
    
    @staticmethod
    def save(db: Session, project: Project) -> Project:
        if not project.id:
            db.add(project)
        else:
            db.merge(project)
        db.commit()
        db.refresh(project)
        return project
    
    @staticmethod
    def delete(db: Session, project: Project) -> Project:
        db.delete(project)
        db.commit()
        return project
    
    @staticmethod
    def delete_by_id(db: Session, id: int) -> Project:
        project = ProjectRepository.get_by_id(db, id)
        db.delete(project)
        db.commit()
        return project
    
    @staticmethod
    def delete_by_name(db: Session, name: str) -> Project:
        project = ProjectRepository.get_by_name(db, name)
        db.delete(project)
        db.commit()
        return project